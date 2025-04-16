document.querySelector('form').addEventListener('submit', function (e) {
    const fileInput = document.getElementById('file');
    const mode = document.querySelector('input[name="mode"]:checked').value;

    if (!fileInput.files.length) return; 

    const file = fileInput.files[0];

    if (mode === "overwrite" && file.size < 100) { 
        const confirmEmpty = confirm("The file you're uploading appears to be very small or empty. Empty template will erase your current bookshelf. Are you sure you want to continue?");
        if (!confirmEmpty) {
            e.preventDefault(); 
        }
    }
});

