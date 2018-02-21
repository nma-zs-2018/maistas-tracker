function orderButton() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(submit, showError);
    } else {
        alert('Location not supported');
    }
}

function showError(error) {
    errorString = '';
    switch (error.code) {
        case error.PERMISSION_DENIED:
            errorString = 'User denied the location request.';
            break;
        case error.POSITION_UNAVAILABLE:
            errorString = 'Location information is unavailable.';
            break;
        case error.TIMEOUT:
            errorString = 'Location request timed out.';
            break;
        default:
            errorString = 'An unknown error occured.';
            break;
    }
    alert(errorString);
}

function submit(position) {
    var token = document.getElementsByName("csrfmiddlewaretoken")[0];
    var tokenName = token.name;
    var tokenValue = token.value;

    var form = document.getElementById('orderForm').getElementsByTagName('input');
    var data = [];
    for (var i = 0; i < form.length; i++) {
        data.push({name: form[i].name, value: form[i].value});
    }
    data.push({name: 'lat', value: position.coords.latitude});
    data.push({name: 'long', value: position.coords.longitude});
    data.push({name: tokenName, value: tokenValue});

    console.log(data);

    $.post('/order/', data, function (data, status) {
        if (data['success'] === false) {
            alert('Unable to make the order: ' + data['error_message']);
            return false;
        }

        if (status !== 'success') {
            alert('Unable to make the order: unknown error.');
            return false;
        }

        alert('Order successful!');
        location.reload(true);
        return true;
    });
}