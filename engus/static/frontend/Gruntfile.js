module.exports = function(grunt) {

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        uglify: {
            options: {
                banner: '/*! <%= pkg.name %> - v<%= pkg.version %> - <%= grunt.template.today("dd-mm-yyyy") %> */\n'
            },
            dist: {
                files: {
                    '../js/global.min.js': [
                        'bower_components/jquery/dist/jquery.min.js',
                        'scripts/card-create-ajax.js',
                        'scripts/card-list.js',
                        'scripts/card.js'
                    ]
                }
            }
        },
        stylus: {
            compile: {
                options: {
                    compress: false
                },
                files: {
                    'tmp/global.stylus.css': 'stylus/global.styl'
                }
            }
        },
        csso: {
            dist: {
                files: {
                    '../css/global.min.css': [
                        'tmp/global.stylus.css'
                    ]
                }
            }
        },
        watch: {
            files: ['stylus/**', 'scripts/**'],
            tasks: ['stylus', 'csso', 'uglify']
        }
    });

    grunt.loadNpmTasks('grunt-contrib-stylus');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-csso');

    grunt.registerTask('default', ['uglify', 'stylus', 'csso']);

};
