document.getElementById('chat-input').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        var question = event.target.value;
        event.target.value = '';

        fetch('/ask_question', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question: question })
        })
        .then(response => response.json())
        .then(data => {
            var chatOutput = document.getElementById('chat-output');
            chatOutput.innerHTML += `<div>User: ${question}</div>`;

            // 使用data.result来获取响应文本，并替换换行符为HTML的<br>标签
            var botResponse = (data.result || 'No response').replace(/\n/g, '<br>');
            chatOutput.innerHTML += `<div>Bot: ${botResponse}</div>`;

            chatOutput.scrollTop = chatOutput.scrollHeight;
        });
    }
});
