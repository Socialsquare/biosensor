// 1. LIBRARIES
// - - - - - - - - - - - - - - -

var gulp = require('gulp');
var autoprefixer = require('gulp-autoprefixer');
var concat = require('gulp-concat');
var minifycss = require('gulp-minify-css');
var livereload = require('gulp-livereload');
var minify = require('gulp-minify');
var rename = require('gulp-rename');
var rimraf = require('rimraf');
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
      'biosensor/static/biosensor/javascript/*.js',
      'node_modules/bootstrap/dist/js/bootstrap.js',
      'node_modules/svg4everybody/dist/svg4everybody.js'
    ],
    favicon: [
      'biosensor/static/biosensor/favicon.ico'
    ],
    svg: [
      'biosensor/static/biosensor/images/sprite/*.svg'
    ]
}

// 3. TASKS
// - - - - - - - - - - - - - - -

// Cleans the build directory
gulp.task('clean', function(cb) {
  rimraf('./staticfiles/*', cb);
})

// Compiles Sass
gulp.task('sass', function() {
    return gulp.src(paths.sass)
    .pipe(sass())
    .pipe(autoprefixer({browsers: ['last 2 versions', 'ie 10']}))
    .pipe(gulp.dest('.tmp/css'))
    .pipe(rename({suffix: '.min'}))
    .pipe(minifycss())
    .pipe(gulp.dest('staticfiles/css'))
    .pipe(livereload());
});

// Compiles JS
gulp.task('js', function() {
  return gulp.src(paths.js)
    .pipe(concat('base.js'))
    .pipe(gulp.dest('staticfiles/js'))
    .pipe(rename('base.js'))
    .pipe(minify())
    .pipe(gulp.dest('staticfiles/js'))
    .pipe(livereload());
});

// Copy favicon
gulp.task('copyfav', function() {
  return gulp.src(paths.favicon)
    .pipe(gulp.dest('staticfiles/'))
    .pipe(livereload());
});

// Create SVG sprite
gulp.task('svg-sprite', function() {
  return gulp.src(paths.svg)
    .pipe(svgmin())
    .pipe(rename({prefix: 'sprite_'}))
    .pipe(svgstore())
    .pipe(gulp.dest('staticfiles/'))
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
gulp.task('build', ['sass', 'js', 'svg-sprite', 'copyfav']);

// Default task: builds your app, starts a server, and recompiles assets when they change
gulp.task('default', ['sass', 'js', 'svg-sprite', 'copyfav', 'watch']);
