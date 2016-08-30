(function () {
    'use strict';

    angular
        .module('homepage.avisame.pe')
        .directive('apSearchOption', search_option_directive);

    function search_option_directive() {
        var template = '<div style="background-color: {{ color }}"  class="ap-search-option">' +
            '<div class="ap-search-option-icon">' +
            '<span class="glyphicon glyphicon-{{ icon }}"></span>' +
            '</div>' +
            '<ng-transclude class="ap-search-option-description" style="background-color: {{ changedColor }}">'+
            '</ng-transclude>' +
            '</div>';

        return {
            restrict: 'E',
            transclude: true,
            template: template,
            scope: {
                'color': '@',
                'icon': '@'
            },
            controller: [
                '$scope',
                'changeColor',
                function ($scope, changeColor) {
                    $scope.changedColor = changeColor($scope.color, -20);
                }
            ]
        }
    }
})();
