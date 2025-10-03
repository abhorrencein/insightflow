def process_surveycto_file(df):
    if df.empty:
        raise ValueError("Empty file")
    
    # Drop metadata rows
    df = df.dropna(subset=[df.columns[0]], how='all')
    
    # Remove SurveyCTO metadata
    metadata_cols = {'starttime', 'endtime', 'deviceimei', 'subscriberid', '_version_'}
    clean_df = df.drop(columns=[c for c in df.columns if c in metadata_cols], errors='ignore')
    
    # Schema inference
    categorical_vars = []
    for col in clean_df.columns:
        if clean_df[col].dtype == 'object' and 1 < clean_df[col].nunique() < 15:
            categorical_vars.append({"name": col, "count": clean_df[col].nunique()})
    
    # Completeness score
    completeness = sum(1 for col in clean_df.columns if clean_df[col].isnull().mean() < 0.1) / len(clean_df.columns)
    
    return {
        "response_count": len(clean_df),
        "completeness": completeness,
        "categorical_vars": categorical_vars[:4],  # Top 4
        "has_gps": any('lat' in col.lower() for col in clean_df.columns)
    }
