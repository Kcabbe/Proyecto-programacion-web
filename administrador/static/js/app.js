const noticias = document.getElementById('noticias')

document.addEventListener("DOMContentLoaded", e => {
    fetchData()
})

const fetchData = async () => {
    try {
        const res = await fetch('https://spaceflightnewsapi.net/api/v2/articles')
        const data = await res.json()
        banderillas(data)
    } catch (error) {
        console.log(error)
    }
}

const banderillas = data => {
    let elementos = ''
    data.forEach(item => {
        elementos += `
        <article class="card">
                <img src="${item.imageUrl}" alt="" class="img-fluid">
                <div class="noti">
                    <h3>Titulo: ${item.title}</h3>

                    <p>
                        ${item.summary}
                    </p>
                </div>
            </article>
        `
    });
    noticias.innerHTML = elementos
}