    if (window.parent === window) {
      window.location.href = '/'
    }

    function close() {
      window.parent.removeModalIfOpen();
    }

    window.onload = function() {
      document.getElementById('close').addEventListener('click', close)
    }
