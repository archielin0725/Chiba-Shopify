const drawer = document.querySelector('#filters-drawer');
const panel = drawer?.querySelector('dialog');

if (drawer && panel) {
  const desktopQuery = window.matchMedia('(min-width: 990px)');

  const positionPopover = () => {
    if (!desktopQuery.matches || !drawer.hasAttribute('open')) return;

    const trigger = document.querySelector('.facets-drawer-trigger');
    if (!trigger) return;

    const rect = trigger.getBoundingClientRect();
    const width = Math.min(320, window.innerWidth - 32);
    const left = Math.max(16, Math.min(rect.left, window.innerWidth - width - 16));
    const top = Math.max(16, Math.min(rect.bottom + 8, window.innerHeight - 260));

    panel.style.setProperty('--filters-popover-left', `${left}px`);
    panel.style.setProperty('--filters-popover-top', `${top}px`);
  };

  document.addEventListener('theme-drawer:open', (event) => {
    if (event.target === drawer) positionPopover();
  });

  document.addEventListener(
    'pointerdown',
    (event) => {
      if (!desktopQuery.matches || !drawer.hasAttribute('open')) return;

      const trigger = document.querySelector('.facets-drawer-trigger');
      if (panel.contains(event.target) || trigger?.contains(event.target)) return;

      drawer.close();
    },
    true
  );

  window.addEventListener('resize', positionPopover);
  window.addEventListener('scroll', positionPopover, true);
}
