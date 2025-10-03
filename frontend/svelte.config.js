import adapter from '@sveltejs/adapter-auto';

/** @type {import('@sveltejs/kit').Config} */
const config = {
  kit: {
    // adapter auto selects the appropriate adapter based on environment
    adapter: adapter()
  }
};

export default config;
