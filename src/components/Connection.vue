<template>
    <form id="upload-container" method="POST" action="/image">
        <img id="upload-image" src="../static/imgs/upload.svg">
        <div>
            <input id="file-input" type="file" name="file" multiple>
            <label for="file-input">Выберите файл</label>
            <span>или перетащите его сюда</span>
        </div>
    </form>
</template>

<script>
$(document).ready(function() {
    var dropZone = $('#upload-container');
    $('#file-input').focus(function() {
        $('label').addClass('focus');
    }).focusout(function() {
        $('label').removeClass('focus');
    });
    dropZone.on('drag dragstart dragend dragover dragenter dragleave drop', function() {
        return false;
    });
    dropZone.on('dragover dragenter', function() {
        dropZone.addClass('dragover');
    });
    dropZone.on('dragleave', function(e) {
        let dx = e.pageX - dropZone.offset().left;
        let dy = e.pageY - dropZone.offset().top;
        if ((dx < 0) || (dx > dropZone.width()) || (dy < 0) || (dy > dropZone.height())) {
            dropZone.removeClass('dragover');
        }
    });
    dropZone.on('drop', function(e) {
        dropZone.removeClass('dragover');
        let files = e.originalEvent.dataTransfer.files;
        sendFiles(files);
    });
    $('#file-input').change(function() {
        let files = this.files;
        sendFiles(files);
    });

    function sendFiles(files) {
        let maxFileSize = 5242880;
        let Data = new FormData();
        $(files).each(function(index, file) {
            if ((file.type == 'image/jpg') || (file.type == 'image/jpeg')) {
                Data.append('image', file);
            };
        });
        $.ajax({
            url: 'http://127.0.0.1:8000/image',
            type: dropZone.attr('method'),
            data: Data,
            contentType: false,
            processData: false,
            success: function(data) {
                // pop up window with result here
                alert(JSON.stringify(data));
            }
        });
    }
})
</script>

<style>
body {
     padding: 0;
     margin: 0;
     display: flex;
     justify-content: center;
     align-items: center;
     min-height: 100vh;
}

#upload-container {
     display: flex;
     justify-content: center;
     align-items: center;
     flex-direction: column;
     width: 400px;
     height: 400px;
     outline: 2px dashed #5d5d5d;
     outline-offset: -12px;
     background-color: #e0f2f7;
     font-family: 'Segoe UI';
     color: #1f3c44;
}

#upload-container img {
     width: 40%;
     margin-bottom: 20px;
     user-select: none;
}

#upload-container label {
     font-weight: bold;
}

#upload-container label:hover {
     cursor: pointer;
     text-decoration: underline;
}

#upload-container div {
     position: relative;
     z-index: 10;
}

#upload-container input[type=file] {
     width: 0.1px;
     height: 0.1px;
     opacity: 0;
     position: absolute;
     z-index: -10;
}

#upload-container label.focus {
     outline: 1px solid #0078d7;
     outline: -webkit-focus-ring-color auto 5px;
}
</style>
