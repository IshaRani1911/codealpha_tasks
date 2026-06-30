const copyButton = document.getElementById("copyBtn");

copyButton.addEventListener("click", function () {

    const outputText = document.getElementById("outputText").value;

    if (outputText.trim() === "") {
        alert("Nothing to copy!");
        return;
    }

    navigator.clipboard.writeText(outputText);

    copyButton.innerText = "Copied!";

    setTimeout(function () {
        copyButton.innerText = "Copy";
    }, 2000);

});


const speakButton = document.getElementById("speakBtn");

speakButton.addEventListener("click", function () {

    const text = document.getElementById("outputText").value;
    const target = document.getElementById("targetLanguageHidden").value;

    if (text.trim() === "") {
        alert("Nothing to speak!");
        return;
    }

    fetch("/speak", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            text: text,
            target: target
        })
    })
    .then(response => response.blob())
    .then(blob => {

        const audioUrl = URL.createObjectURL(blob);

        const audio = new Audio(audioUrl);

        audio.play();

    });

});
