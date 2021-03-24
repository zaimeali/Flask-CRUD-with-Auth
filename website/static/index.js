const deleteNote = (id) => {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({
      noteId: id,
    }),
  }).then((res) => (window.location.href = "/"));
};
