async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value;
  input.value = "";

  const chatBox = document.getElementById("chat-box");
  chatBox.innerHTML += `<div class='user'><b>Toi:</b> ${message}</div>`;

  const response = await fetch("http://127.0.0.1:8000/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({message: message})
  });
  const data = await response.json();

  chatBox.innerHTML += `<div class='ai'><b>IA:</b> ${data.reply}</div>`;
  chatBox.scrollTop = chatBox.scrollHeight;
}
