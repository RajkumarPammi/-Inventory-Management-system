const API_URL = 'https://q67qwqgr71.execute-api.us-east-1.amazonaws.com/dev/items';

async function fetchItems() {
    const response = await fetch(API_URL);
    const items = await response.json();
    const list = document.getElementById('inventory-list');
    list.innerHTML = items.map(item => `<p>${item.name}: ${item.quantity}</p>`).join('');
}

document.getElementById('add-item-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const quantity = document.getElementById('quantity').value;
    await fetch(API_URL, {
        method: 'POST',
        body: JSON.stringify({ name, quantity }),
        headers: { 'Content-Type': 'application/json' }
    });
    fetchItems();
});

fetchItems();