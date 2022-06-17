(function () {
    angular
        .module('services.avisame.pe', [])
        .factory('changeColor', changeColor);

    function changeColor() {
        return fnc;

        function fnc(color, plus) {
            if (color[0] == '#') {
                color = color.slice(1);
            }
            var rgb = parseInt(color, 16);
            var r = Math.max(Math.min((rgb >> 16) + plus, 255), 0);
            var g = Math.max(Math.min(((rgb >> 8) & 0x00FF) + plus, 255), 0);
            var b = Math.max(Math.min((rgb & 0x0000FF) + plus, 255), 0);
            var hex = ((r << 16) | (g << 8) | b).toString(16);
            return '#000000'.substr(0, 7 - hex.length) + hex;
        }
    }
})();
