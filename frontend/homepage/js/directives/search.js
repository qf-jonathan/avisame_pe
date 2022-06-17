(function () {
    'use strict';

    angular
        .module('homepage.avisame.pe')
        .directive('apSearch', search_directive);

    function search_directive() {
        return {
            templateUrl: '/search-template.html',
            controller: [
                '$scope',
                function ($scope) {

                }
            ]
        }
    }
})();
