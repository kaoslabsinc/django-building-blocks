function runStackEditCode(elId, name) {
  const stackedit = new Stackedit();
  const el = document.getElementById(elId);
  stackedit.openFile({
    name,
    content: {
      text: el.value
    }
  });
  stackedit.on('fileChange', function (file) {
    el.value = file.content.text;
  });
}
