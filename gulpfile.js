// 1. LIBRARIES
// - - - - - - - - - - - - - - -

var gulp = require('gulp');
var sass = require('gulp-sass');
var autoprefixer = require('gulp-autoprefixer');
var minifycss = require('gulp-minify-css');
var rename = require('gulp-rename');
var watch = require('gulp-watch');
var livereload = require('gulp-livereload');
var uglify = require('gulp-uglify');
var rimraf = require('rimraf');

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
gulp.task('uglify', function() {
  return gulp.src(paths.js)
    //.pipe(uglify().on('error', function(e){
    //    console.log(e);
    // }))
    .pipe(gulp.dest('staticfiles/js'))
    .pipe(livereload());
});

gulp.task('copyjs', function() {
    return gulp.src(paths.js)
    .pipe(gulp.dest('staticfiles/js'))
    .pipe(livereload());
});

gulp.task('watch', function() {
    livereload.listen();

    // Watch Sass
    gulp.watch(paths.sassWatch, ['sass']);

    // Watch javascript
    gulp.watch(paths.js, ['copyjs']);

    // Watch Django temlates
    gulp.watch('**/templates/*').on('change', livereload.changed);

});

// Builds your entire app once, without starting a server
gulp.task('build', ['sass', 'uglify']);

// Default task: builds your app, starts a server, and recompiles assets when they change
gulp.task('default', ['sass', 'copyjs', 'watch']);
