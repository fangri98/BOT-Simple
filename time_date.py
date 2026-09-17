from datetime import datetime as dt

def waktu_sekarang():
    """Mengembalikan waktu sekarang dalam format jam:menit:detik"""
    return dt.now().strftime("%H:%M:%S")
def tanggal_sekarang():
    """Mengembalikan tanggal sekarang dalam format hari/bulan/tahun"""
    return dt.now().strftime("%d/%m/%Y")