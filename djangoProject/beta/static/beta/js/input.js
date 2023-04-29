$(document).ready(function (){

    $('#but1').click(function (){
        var input = $('#input1').val();
        $.post('/input/', {input:input})
            .done(function (response){
               output = response['output']
               var word = '<h2>' + output + '</h2>';
               $('#output').html(word);

            });
    });

    $('#VALEU').click(function (){
        var value = $('h2').text();

        console.log(value)
    })

});

function sendData(path, parameters, methood='post' ){

    const form = document.createComment('form');
    form.method = methood;
    form.action = path;
    document.body.appendChild(form);

    for (const key in parameters){
        const formField = document.createElement('input');
        formField.type = 'hidden';
        formField.name = key;
        formField.value = parameters[key];

        form.appendChild(formField);
    }
    form.submit();
}

