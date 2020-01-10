var modalId = 'movie-modal';
var backdropId = 'modal-backdrop';

function openModal(id) {
  removeModalIfOpen();
  var backdrop = document.createElement('div');
  backdrop.id = backdropId;
  backdrop.addEventListener('click', removeModalIfOpen);

  var modal = document.createElement('modal');
  modal.id = modalId;

  var iframe = document.createElement('iframe');
  iframe.src = '/movies/' + id;

  modal.appendChild(iframe);
  document.body.appendChild(modal);
  document.body.appendChild(backdrop);

  window.addEventListener('keyup', (e) => {
    if (!e) e = window.event;
    var keyCode = e.keyCode || e.which;
    if (keyCode == '27') {
      removeModalIfOpen();
    }
  })
}

function removeModalIfOpen() {
  var modal = document.getElementById(modalId);
  var backdrop = document.getElementById(backdropId);
  if (modal) {
    modal.remove();
  }

  if (backdrop) {
    backdrop.remove();
  }
}
