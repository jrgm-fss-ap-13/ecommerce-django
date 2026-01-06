// Inicialización del slider de miniaturas
const sliderThumbs = new Swiper(".slider__thumbs .swiper-container", {
  // buscamos el slider de miniaturas por selector y establecemos los parámetros
  direction: "vertical", // desplazamiento vertical
  slidesPerView: 4, // mostrar 3 miniaturas
  spaceBetween: 24, // espacio entre miniaturas
  mousewheel: true,
  navigation: {
  // establecemos los botones de navegación
  nextEl: ".slider__next", // botón siguiente
  prevEl: ".slider__prev" // botón anterior
  },
  freeMode: true, // cuando arrastras la miniatura, se comporta como scroll
  breakpoints: {
  // condiciones para diferentes tamaños de pantalla
  0: {
  // cuando es 0px o más grande
  direction: "horizontal" // desplazamiento horizontal
  },
  768: {
  // cuando es 768px o más grande
  direction: "vertical" // desplazamiento vertical
  }
  }
  });
  // Inicialización del slider de imágenes
  const sliderImages = new Swiper(".slider__images .swiper-container", {
  // buscamos el slider de imágenes por selector y establecemos los parámetros
  direction: "vertical", // desplazamiento vertical
  slidesPerView: 1, // mostrar 1 imagen
  spaceBetween: 32, // espacio entre imágenes
  mousewheel: true, // se puede desplazar las imágenes con la rueda del ratón
  navigation: {
  // establecemos los botones de navegación
  nextEl: ".slider__next", // botón siguiente
  prevEl: ".slider__prev" // botón anterior
  },
  grabCursor: true, // cambiar el cursor del ratón
  thumbs: {
  // indicamos el slider de miniaturas
  swiper: sliderThumbs // indicamos el nombre del slider de miniaturas
  },
  breakpoints: {
  // condiciones para diferentes tamaños de pantalla
  0: {
  // cuando es 0px o más grande
  direction: "horizontal" // desplazamiento horizontal
  },
  768: {
  // cuando es 768px o más grande
  direction: "vertical" // desplazamiento vertical
  }
  }
  });