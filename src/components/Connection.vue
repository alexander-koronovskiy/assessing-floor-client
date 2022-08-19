<template>
    <form id="upload-container" method="POST" action="/image">
        <img id="upload-image" src="assets/upload.svg">
        <div>
            <input id="file-input" type="file" name="file" multiple>
            <label for="file-input">Выберите файл</label>
            <span>или перетащите его сюда</span>
        </div>
    </form>
</template>

<script>
 export default {
    mounted() {
        let maxFileSize = 5242880;
        let Data = new FormData();
        Data.append('image', '');
        fetch('http://127.0.0.1:8000/image', {
            method: "POST",
            body: Data
        }).then(response => {
            if (response.status !== 200) {
                return Promise.reject();
            }
            return response.json();
        }).then(function(data) {
            alert(JSON.stringify(data))
        }).catch(() => alert('ошибка'));
    }
}
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
