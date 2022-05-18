const request = new XMLHttpRequest()

window.addEventListener("load", function() {
    (function($) {
        $("#id_Search_For_EDV").change(function() {
            request.open('GET', "http://localhost:8000/colabs/?edv=" + document.getElementById("id_Search_For_EDV").value)
            request.onload = function () {
                console.log(JSON.parse(this.responseText))
            }
            request.onerror = function () {
                console.log('erro ao executar a requisição')
            }
            request.send()
        });
    })(django.jQuery);
});