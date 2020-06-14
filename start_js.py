import os
import sys

USER_PATH_DIR = os.getcwd()
PROJECT_NAME = sys.argv[1]
PROJECT_PATH = os.path.join(USER_PATH_DIR, PROJECT_NAME)
def make_project_dir():
    try:
        os.mkdir(PROJECT_PATH)
    except OSError:
        pass

def make_src_dir():
    src_dir = os.path.join(PROJECT_PATH, 'src')
    try:
        os.mkdir(src_dir)
    except OSError:
        pass
    js_path = os.path.join(src_dir, 'js')
    try:
        os.mkdir(js_path)
    except OSError:
        pass
    main_path = os.path.join(js_path, 'main.js')
    open(main_path, 'w').close() 
    index_path = os.path.join(src_dir, 'index.html')
    open(index_path, 'w').close()    


def make_gulp():
    with open('gulpfile.js', 'w', encoding="utf-8") as file:
        file.write('''
"use strict";

const gulp = require("gulp");
const webpack = require("webpack-stream");
const browsersync = require("browser-sync");

const dist = "./dist/";
// const dist = "/Applications/MAMP/htdocs/test";

gulp.task("copy-html", () => {
  return gulp.src("./src/index.html")
    .pipe(gulp.dest(dist))
    .pipe(browsersync.stream());
});

gulp.task("build-js", () => {
  return gulp.src("./src/js/main.js")
    .pipe(webpack({
      mode: 'development',
      output: {
        filename: 'script.js'
      },
      watch: false,
      devtool: "source-map",
      module: {
        rules: [
          {
            test: /\.m?js$/,
            exclude: /(node_modules|bower_components)/,
            use: {
              loader: 'babel-loader',
              options: {
                presets: [['@babel/preset-env', {
                  debug: true,
                  corejs: 3,
                  useBuiltIns: "usage"
                }]]
              }
            }
          }
        ]
      }
    }))
    .pipe(gulp.dest(dist))
    .on("end", browsersync.reload);
});

gulp.task("copy-assets", () => {
  return gulp.src("./src/assets/**/*.*")
    .pipe(gulp.dest(dist + "/assets"))
    .on("end", browsersync.reload);
});

gulp.task("watch", () => {
  browsersync.init({
    server: "./dist/",
    port: 4000,
    notify: true
  });

  gulp.watch("./src/index.html", gulp.parallel("copy-html"));
  gulp.watch("./src/assets/**/*.*", gulp.parallel("copy-assets"));
  gulp.watch("./src/js/**/*.js", gulp.parallel("build-js"));
});

gulp.task("build", gulp.parallel("copy-html", "copy-assets", "build-js"));

gulp.task("build-prod-js", () => {
  return gulp.src("./src/js/main.js")
    .pipe(webpack({
      mode: 'production',
      output: {
        filename: 'script.js'
      },
      module: {
        rules: [
          {
            test: /\.m?js$/,
            exclude: /(node_modules|bower_components)/,
            use: {
              loader: 'babel-loader',
              options: {
                presets: [['@babel/preset-env', {
                  corejs: 3,
                  useBuiltIns: "usage"
                }]]
              }
            }
          }
        ]
      }
    }))
    .pipe(gulp.dest(dist));
});

gulp.task("default", gulp.parallel("watch", "build"));

''')


def make_package_json():
    with open('package.json', 'w', encoding='utf-8') as file:
        file.write('{\n"name": "' + PROJECT_NAME + '",')
        file.write('''
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "author": "",
  "license": "ISC",
  "browserslist": [
    "> 1%",
    "not dead"
  ],
  "devDependencies": {
    "@babel/core": "^7.7.4",
    "@babel/preset-env": "^7.7.4",
    "babel": "^6.23.0",
    "babel-core": "^6.26.3",
    "babel-loader": "^8.0.6",
    "browser-sync": "^2.26.7",
    "core-js": "^3.4.2",
    "gulp": "^4.0.2",
    "webpack": "^4.41.2",
    "webpack-stream": "^5.2.1"
  }
}

''')


def make_gitignore():
    with open('.gitignore', 'w', encoding='utf-8') as file:
        file.write('node_modules')

def npm_install():
    os.system('npm i')

def main():
    make_project_dir()
    os.chdir(PROJECT_PATH)
    make_src_dir()
    make_gulp()
    make_package_json()
    make_gitignore()
    npm_install()


if __name__ == "__main__":
    main()
