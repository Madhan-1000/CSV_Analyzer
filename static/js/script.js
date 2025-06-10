   function enterSite() {
      const intro = document.getElementById('intro');
      const main = document.getElementById('main');
      intro.classList.add('hidden');
      document.body.style.overflow = 'auto';
      setTimeout(() => {
        main.classList.add('show-main');
      }, 800); // Matches the fade-out duration
    }