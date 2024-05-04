// <!-- JavaScript for carousel functionality -->
    let currentStartIndex = 0;
    const totalItems = document.querySelectorAll('.brand-item').length;
    const container = document.querySelector('.carousel-container');
    const carouselInner = document.querySelector('.carousel-container .row');
    const itemWidth = document.querySelector('.brand-item').offsetWidth + 20; // Including margin

    function moveCarousel(direction) {
        const maxIndex = totalItems - Math.floor(container.offsetWidth / itemWidth);
        currentStartIndex += direction;

        if (currentStartIndex < 0) {
            currentStartIndex = 0;
        } else if (currentStartIndex > maxIndex) {
            currentStartIndex = maxIndex;
        }

        const offset = currentStartIndex * -itemWidth;
        carouselInner.style.transform = `translateX(${offset}px)`;
    }
