const sendButton = document.getElementById("sendBtn");
const inputBox = document.getElementById("inputText");
const chatWindow = document.getElementById("chatWindow");

function addMessage(text, sender) {
  const msgDiv = document.createElement("div");
  msgDiv.classList.add("message", sender); // sender = "user" or "bot"
  msgDiv.textContent = text;
  chatWindow.appendChild(msgDiv);
  chatWindow.scrollTop = chatWindow.scrollHeight; // auto-scroll to latest
}

async function sendMessage() {
  const inputText = inputBox.value.trim();
  if (inputText === "") {
    alert("Nothing to send!");
    return;
  }

  addMessage(inputText, "user");
  inputBox.value = "";

  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: inputText })
    });

    const data = await response.json();
    addMessage(data.response, "bot");
  } catch (error) {
    addMessage("Something went wrong. Please try again.", "bot");
    console.error(error);
  }
}

sendButton.addEventListener("click", sendMessage);

// Bonus: allow pressing Enter to send
inputBox.addEventListener("keydown", function (e) {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});