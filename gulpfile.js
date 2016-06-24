// 1. LIBRARIES
// - - - - - - - - - - - - - - -

var gulp = require('gulp');
var autoprefixer = require('gulp-autoprefixer');
var concat = require('gulp-concat');
var del = require('del');
var livereload = require('gulp-livereload');
var minify = require('gulp-minify');
var minifycss = require('gulp-minify-css');
var rename = require('gulp-rename');
var runSequence = require('run-sequence');
var sass = require('gulp-sass');
var svgmin = require('gulp-svgmin');
var svgstore = require('gulp-svgstore');
var watch = require('gulp-watch');

// 2. FILE PATHS
// - - - - - - - - - - - - - - -

var paths = {
    sass: [
      'biosensor/static/biosensor/css/base.scss',
      'bioadmin/static/bioadmin/css/bioadmin.scss',
    ],
    sassWatch: [
      'biosensor/static/biosensor/css/*.scss',
      'bioadmin/static/bioadmin/css/*.scss',
    ],
    js: [
      'node_modules/bootstrap/dist/js/bootstrap.js',
      'node_modules/svg4everybody/dist/svg4everybody.js',
      'biosensor/static/biosensor/javascript/*.js'
    ],
    favicon: [
      'biosensor/static/biosensor/favicon.ico'
    ],
    svg: [
      'biosensor/static/biosensor/images/sprite/*.svg'
    ],
    static: [
      'staticfiles/'
    ]
}

// 3. TASKS
// - - - - - - - - - - - - - - -

// Cleans the build directory
gulp.task('clean', function() {
  return del(paths.static + '*');
})

// Compiles Sass
gulp.task('sass', function() {
    return gulp.src(paths.sass)
    .pipe(sass())
    .pipe(autoprefixer({browsers: ['last 2 versions', 'ie 10']}))
    .pipe(gulp.dest('.tmp/css'))
    .pipe(rename({suffix: '.min'}))
    .pipe(minifycss())
    .pipe(gulp.dest(paths.static + 'css'))
    .pipe(livereload());
});

// Compiles JS
gulp.task('js', function() {
  return gulp.src(paths.js)
    .pipe(concat('base.js'))
    .pipe(gulp.dest(paths.static + 'js'))
    .pipe(rename('base.js'))
    .pipe(minify())
    .pipe(gulp.dest(paths.static + 'js'))
    .pipe(livereload());
});

// Copy favicon
gulp.task('copyfav', function() {
  return gulp.src(paths.favicon)
    .pipe(gulp.dest(paths.static + ''))
    .pipe(livereload());
});

// Create SVG sprite
gulp.task('svg-sprite', function() {
  return gulp.src(paths.svg)
    .pipe(svgmin())
    .pipe(rename({prefix: 'sprite_'}))
    .pipe(svgstore())
    .pipe(gulp.dest(paths.static + ''))
    .pipe(livereload());
});


gulp.task('watch', function() {
    livereload.listen();

    // Watch Sass
    gulp.watch(paths.sassWatch, ['sass']);

    // Watch javascript
    gulp.watch(paths.js, ['js']);

    // Watch svg
    gulp.watch(paths.svg, ['svg-sprite']);

    // Watch Django temlates
    gulp.watch('**/templates/*').on('change', livereload.changed);

});

// Builds your entire app once, without starting a server
gulp.task('build', function(callback) {
  runSequence(
    'clean',
    ['sass', 'js', 'svg-sprite', 'copyfav'],
    callback);
});

// Default task: builds your app, starts a server, and recompiles assets when they change
gulp.task('default', function(callback) {
  runSequence(
    'clean',
    ['sass', 'js', 'svg-sprite', 'copyfav'],
    'watch',
    callback);
});
