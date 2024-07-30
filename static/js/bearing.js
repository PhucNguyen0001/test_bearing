document.querySelector('form').addEventListener('submit', function(event) {
    const d = document.querySelector('input[name="d bore"]').value;
    const D = document.querySelector('input[name="D outside"]').value;
    const B = document.querySelector('input[name="B"]').value;

    let filledFields = 0;
    if (d) filledFields++;
    if (D) filledFields++;
    if (B) filledFields++;

    if (filledFields < 2) {
        alert('Vui lòng điền ít nhất 2 trong 3 trường dữ liệu.');
        event.preventDefault(); // Ngăn chặn form gửi đi
    }
});
