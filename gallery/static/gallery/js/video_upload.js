/**
Provide drag and drop support on video display pages
*/

document.addEventListener('drop', function(event) {
    var drop_container = document.getElementById('video_container');
    var video_form = document.getElementById('video_upload_form');
    var data_input  = video_form.elements['data'];

    drop_container.classList.remove('highlight');

    data_input.files = event.dataTransfer.files;
    video_form.submit();

    event.preventDefault();
});

document.addEventListener('dragover', function(event) {
    event.preventDefault();
});

document.addEventListener('dragenter', function(event) {
    var drop_container = document.getElementById('video_container');
    drop_container.classList.add('highlight');
    event.preventDefault();
});

document.addEventListener('dragexit', function() {
    var drop_container = document.getElementById('video_container');
    drop_container.classList.remove('highlight');
});
