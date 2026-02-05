document.getElementById("contactForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const data = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        message: document.getElementById("message").value
    };

    fetch("http://127.0.0.1:5000/contact", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(result => {
        document.getElementById("response").innerText = result.status;
        document.getElementById("contactForm").reset();
    })
    .catch(() => {
        document.getElementById("response").innerText = "Error sending message";
        document.getElementById("response").style.color = "red";
    });
});
