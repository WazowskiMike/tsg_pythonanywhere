function copyPhoneToClipboard() {
    // Находим элемент с классом "text-light"
    var emailElement = document.querySelector('.company-phone');

    // Создаем временный элемент textarea
    var tempTextArea = document.createElement('textarea');

    // Устанавливаем значение временного элемента равным значению email
    tempTextArea.value = emailElement.textContent.trim();

    // Добавляем временный элемент в DOM
    document.body.appendChild(tempTextArea);

    // Выделяем содержимое временного элемента
    tempTextArea.select();

    // Копируем содержимое в буфер обмена
    document.execCommand('copy');

    // Удаляем временный элемент из DOM
    document.body.removeChild(tempTextArea);

    // Опционально можно вывести сообщение об успешном копировании
    var copyMessageContainer = document.querySelector('.copy-phone-container');
    copyMessageContainer.style.display = 'block';
    setTimeout(function() {
        copyMessageContainer.style.display = 'none';
    }, 2000); // Скрываем сообщение через 2 секунды
}