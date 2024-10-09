



document.addEventListener('DOMContentLoaded', function() {
const avatars = document.querySelectorAll('.avatar-img');
const modal = document.getElementById('avatarModal');
const modalAvatar = document.getElementById('modalAvatar');
const modalUserName = document.getElementById('modalUserName');  // Titulek pro jméno uživatele

avatars.forEach(avatar => {
    avatar.addEventListener('click', function() {
    const avatarSrc = avatar.getAttribute('src');
    const userName = avatar.getAttribute('data-name');  // Získáme jméno uživatele z atributu data-name
    modalAvatar.setAttribute('src', avatarSrc);
    modalUserName.textContent = userName;  // Nastavíme titulek modálního okna na jméno uživatele
    $('#avatarModal').modal('show');
    });
});
});


