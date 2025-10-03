<script>
  let file = null;
  let isUploading = false;
  let result = null;
  let error = null;

  async function handleUpload() {
    if (!file) return;
    
    isUploading = true;
    error = null;
    
    const formData = new FormData();
    formData.append('file', file);
    
    try {
      const res = await fetch('/api/process', {
        method: 'POST',
        body: formData
      });
      
      if (!res.ok) throw new Error('Processing failed');
      result = await res.json();
    } catch (e) {
      error = e.message;
    } finally {
      isUploading = false;
    }
  }
</script>

<div class="p-8 max-w-7xl mx-auto">
  <div class="mb-12">
    <h2 class="text-3xl font-bold text-slate-900">Automated Survey Intelligence</h2>
    <p class="text-slate-600 mt-2 max-w-2xl">
      Upload your SurveyCTO export. We’ll clean, analyze, and visualize — in seconds.
    </p>
  </div>

  {#if !result}
    <div class="border-2 border-dashed border-slate-300 rounded-2xl p-12 text-center bg-white hover:border-primary-300 transition-colors">
      <input 
        type="file" 
        accept=".xlsx" 
        class="hidden" 
        id="file-upload"
        on:change={(e) => file = e.target.files[0]}
      />
      <label for="file-upload" class="cursor-pointer">
        <div class="text-slate-500 mb-3">📤</div>
        <p class="font-medium text-slate-900">Click to upload SurveyCTO XLSX</p>
        <p class="text-sm text-slate-500 mt-1">or drag and drop</p>
      </label>
      
      {#if file}
        <p class="mt-4 text-sm text-slate-600">{file.name}</p>
        <button 
          on:click={handleUpload}
          disabled={isUploading}
          class="mt-4 px-6 py-2.5 bg-primary-600 text-white rounded-lg font-medium hover:bg-primary-700 disabled:opacity-50"
        >
          {isUploading ? 'Analyzing...' : 'Process Survey'}
        </button>
      {/if}
    </div>
    
    {#if error}
      <div class="mt-6 p-4 bg-red-50 border border-red-200 rounded-lg text-red-700">
        ❌ {error}
      </div>
    {/if}
  {:else}
    <!-- DASHBOARD VIEW -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <!-- Summary Cards -->
      <div class="bg-white p-6 rounded-2xl border border-slate-200">
        <h3 class="font-semibold text-slate-900 mb-4">Survey Health</h3>
        <div class="space-y-4">
          <div>
            <p class="text-sm text-slate-500">Responses</p>
            <p class="text-2xl font-bold text-slate-900">{result.response_count}</p>
          </div>
          <div>
            <p class="text-sm text-slate-500">High-Quality Fields</p>
            <p class="text-2xl font-bold text-slate-900">{Math.round(result.completeness * 100)}%</p>
          </div>
        </div>
      </div>
      
      <!-- Map Placeholder -->
      <div class="lg:col-span-2 bg-white p-6 rounded-2xl border border-slate-200">
        <h3 class="font-semibold text-slate-900 mb-4">Field Locations</h3>
        <div class="bg-slate-50 rounded-xl h-64 flex items-center justify-center text-slate-500">
          Interactive map will appear here
        </div>
      </div>
    </div>
    
    <!-- Charts -->
    <div class="mt-
