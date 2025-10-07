document.addEventListener('DOMContentLoaded', () => {
  const menuToggle = document.getElementById('menuToggle');
  const menuPanel = document.getElementById('menuPanel');
  const overlay = document.getElementById('overlay');
  const header = document.querySelector('.header');
  const langBtn = document.getElementById('lang-btn');
  const langDropdown = document.getElementById('lang-dropdown');

  // Menyu toggle (ochish/yopish)
  menuToggle.addEventListener('click', (e) => {
    e.stopPropagation();

    if (menuPanel.classList.contains('active')) {
      // Menyu ochiq — yopamiz
      menuPanel.classList.remove('active');
      overlay.classList.remove('active');
      header.classList.remove('menu-open'); // Header qaytadi
      menuToggle.textContent = '☰'; // Iconni qaytarish
    } else {
      // Menyu yopiq — ochamiz
      menuPanel.classList.add('active');
      overlay.classList.add('active');
      header.classList.add('menu-open'); // Header chapga suriladi
      menuToggle.textContent = '☰'; // Iconni o'zgartirish
    }
  });

  // Tashqariga bosilganda yopish
  overlay.addEventListener('click', () => {
    menuPanel.classList.remove('active');
    overlay.classList.remove('active');
    header.classList.remove('menu-open');
    menuToggle.textContent = '☰';
  });

  // Til tanlash dropdown
  langBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    langDropdown.style.display = langDropdown.style.display === 'block' ? 'none' : 'block';
  });

  // Barcha tashqi bosishlarda dropdown yopilsin
  document.addEventListener('click', () => {
    langDropdown.style.display = 'none';
  });

  // Menyu ichidagi linklarga bosilsa ham yopilsin
  document.querySelectorAll('.menu-item').forEach(item => {
    item.addEventListener('click', () => {
      menuPanel.classList.remove('active');
      overlay.classList.remove('active');
      header.classList.remove('menu-open');
      menuToggle.textContent = '☰';
    });
  });
});