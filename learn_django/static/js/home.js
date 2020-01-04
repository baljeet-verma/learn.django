
function onRegistrationFormSubmitted(event) {

    event.preventDefault();
    event.stopPropagation();

    var form = event.target;

    form.classList.add('was-validated');

    if (form.checkValidity() == false)
        return;

    $.ajax({
        url: event.target.action,
        data: new FormData(event.target),
        processData: false,
        contentType: false,
        type: event.target.method,
        success: function (response) {

        }
    });
}