function solve() {
  // test()

  document.getElementsByTagName('button')[0].addEventListener('click', addTableRows);

  document.getElementsByTagName('button')[1].addEventListener('click', buySelectedFurniture)


  function addTableRows() {
    let parsedArr = JSON.parse(document.querySelector("#exercise textarea").value);

    let tableBody = document.getElementsByTagName('tbody')[0];
    for (let obj of parsedArr) {
      let tableRow = createTableRow(obj);
      tableBody.appendChild(tableRow);
    };

  };


  function createTableRow(obj) {
    let tableRow = document.createElement('tr');
    let img = document.createElement('img');
    img.setAttribute('src', obj['img']);

    let imgTd = document.createElement('td');
    imgTd.appendChild(img);

    let nameTd = document.createElement('td');
    nameTd.innerHTML = `<p>${obj['name']}</p>`;

    let priceTd = document.createElement('td');
    priceTd.innerHTML = `<p>${obj['price']}</p>`;

    let decFactorTd = document.createElement('td');
    decFactorTd.innerHTML = `<p>${obj['decFactor']}</p>`;


    let checkboxInput = document.createElement('input');
    checkboxInput.setAttribute('type', 'checkbox');
    // checkboxInput.disabled = true;

    let checkBoxTd = document.createElement('td');
    checkBoxTd.appendChild(checkboxInput);

    tableRow.appendChild(imgTd);
    tableRow.appendChild(nameTd);
    tableRow.appendChild(priceTd);
    tableRow.appendChild(decFactorTd);
    tableRow.appendChild(checkBoxTd);

    return tableRow
  };

  function buySelectedFurniture() {
    let selectedInputs = document.querySelectorAll('td input[type="checkbox"]:checked')
    let totalPrice = 0;
    let decFacSum = 0;
    let furnitureName = [];

    for (let selected of selectedInputs) {
      let parentRowElement = selected.parentNode.parentNode;
      let [_, name, price, decFac, __] = parentRowElement.children;
      [name, price, decFac] = [name.textContent, Number(price.textContent), Number(decFac.textContent)];

      totalPrice += price;
      decFacSum += decFac;
      furnitureName.push(name);
    };

    let outputArea = document.getElementsByTagName('textarea')[1];
    outputArea.value += `Bought furniture: ${furnitureName.join(', ')}` + '\n';
    outputArea.value += `Total price: ${totalPrice.toFixed(2)}` + '\n';
    outputArea.value += `Average decoration factor: ${decFacSum / furnitureName.length}`;

    outputArea.value = text;
  };


  function test() {
    // let testJSON = JSON.stringify([
    //   {
    //     "img": "https://www.ikea.com/PIAimages/0447583_PE597395_S5.JPG",
    //     "name": "Sofa",
    //     "price": "259",
    //     "decFactor": "0.4"

    //   },
    //   {
    //     "img": "https://www.stylespafurniture.com/wp-content/uploads/2020/03/Cove_3_Door_Wardrobe_1.jpg",
    //     "name": "Wardrobe",
    //     "price": "120",
    //     "decFactor": "1.2"
    //   }
    // ]);
    // let testJSON = JSON.stringify([{ "name": "Sofa", "img": "https://res.cloudinary.com/maisonsdumonde/image/upload/q_auto,f_auto/w_200/img/grey-3-seater-sofa-bed-200-13-0-175521_9.jpg", "price": 150, "decFactor": 1.2 }]);
    let testJSON = JSON.stringify([{ "name": "Tablet", "img": "https://s12emagst.akamaized.net/products/16498/16497603/images/res_aec28fc5950c2a40e001ff99795e576b_200x200_l6m7.jpg", "price": 2000, "decFactor": 5.2 }, { "name": "Vase", "img": "https://cdn.shoplightspeed.com/shops/606957/files/11398239/200x200x2/small-lady-vase.jpg", "price": 15, "decFactor": 10 }]);

    document.querySelector('#exercise textarea').value = testJSON;

  };
}