/** Justify image grid based on thumbnail class

    These global vars should be present

    hdpi_factor e.g. 2
    image_margin e.g 6.0

*/



function justify_videos() {
/** Fix the width each image in a container to fully justify each row */

    var container = document.getElementById('image_container')
    // Get exact width of container - 1 to allow for rounding error
    var container_width = container.getBoundingClientRect()['width'] - 1 ;

    // Find the images in the thumbnail container
    var videos = document.querySelectorAll('.video');
    if (videos == []) {
        return;
    }
    // Assume all images have the same height from the ImageSpecField resize
    // var target_height = images[0].naturalHeight / hdpi_factor;

    // Build an array of images for the current row and it's width
    var row_width = 0;
    var row_videos = [];
    for (var i=0; i < videos.length; i++) {
        // Add the current image and it's width
        row_videos.push(videos[i]);
        row_width += (videos[i].naturalWidth / hdpi_factor);
        // Look ahead to see how wide the next image is
        var next_half_width = 0;
        if (i < videos.length - 1) {
            next_half_width = videos[i+1].naturalWidth / hdpi_factor / 2 ;
        }
        // See if the we have exceed the size of the row, including half the next image
        // This keeps us closer to the target height
        if ((row_width + next_half_width) >= container_width) {
            // Account for the total width of all margins on this row
            var margin_total = video_margin * (row_videos.length - 1);
            // Find the factor required to shrink or enlarge the images in this row
            var resize_factor = (container_width - margin_total) / (row_width - margin_total);
            resize_row(row_videos, resize_factor);
            // Reset values for new row
            row_width = 0;
            row_videos = [];
        } else {
            // Add the margin to the running row width
            row_width += video_margin;
        }
        // If there are any orphans on an incomplete last row, resize these
        if (row_width && i == video.length - 1) {
            resize_row(row_videos, resize_factor);
        }

    }

}

function resize_row(videos, factor) {
/** Set each item in the image array according to the given factor */

    for (var i=0; i < videos.length; i++) {

        var width = ((videos[i].naturalWidth / hdpi_factor) * factor);
        videos[i].style.width = width + "px";
        var height = ((videos[i].naturalHeight / hdpi_factor) * factor);
        videos[i].style.height = height + "px";
        // Add a margin if this is not the last image
        if (i < (videos.length - 1)) {
            videos[i].style.marginRight = video_margin + 'px';
        } else {
            videos[i].style.marginRight = '0';
        }
    }
}

window.addEventListener('resize',justify_videos);
