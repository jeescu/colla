
    var panel = document.getElementById('panel'),
        menu = document.getElementById('menu'),
        // demo defaults
        effect = 'mfb-zoomin',
        pos = 'mfb-component--br';

    function _toggleCode() {
      panel.classList.toggle('viewCode');
    }

    function switchEffect(e){
      effect = this.options[this.selectedIndex].value;
      renderMenu();
    }

    function switchPos(e){
      pos = this.options[this.selectedIndex].value;
      renderMenu();
    }

    function renderMenu() {
      menu.style.display = 'none';
      // ?:-)
      setTimeout(function() {
        menu.style.display = 'block';
        menu.className = pos + effect;
      },1);
    }
