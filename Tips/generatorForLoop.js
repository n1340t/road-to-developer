function* listsGenerator() {
  const lists = document.querySelectorAll(
    'a.materials__title.link--download[href*=service]'
  );
  for (const materials of lists) {
    yield materials;
  }
}
const listGen = listsGenerator();
let interval = setInterval(
  function (listGen) {
    const val = listGen.next();
    if (val.done) {
      clearInterval(interval);
    } else {
      val.value.click()
    }
  },
  3000,
  listGen
);
