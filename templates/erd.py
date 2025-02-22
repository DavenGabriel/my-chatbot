from graphviz import Digraph

# Membuat ERD menggunakan Graphviz
erd = Digraph('ERD', filename='erd_murid_guru_admin', format='png')

# Node untuk setiap entitas
erd.node('User', 'User\n(id_user, nama, email, password, role)')
erd.node('Kelas', 'Kelas\n(id_kelas, nama_kelas, deskripsi, id_guru)')
erd.node('Kelas_Murid', 'Kelas_Murid\n(id_kelas, id_murid)')
erd.node('Tugas', 'Tugas\n(id_tugas, judul, deskripsi, deadline, id_kelas, id_guru)')
erd.node('Pengumpulan_Tugas', 'Pengumpulan_Tugas\n(id_pengumpulan, id_tugas, id_murid, file, tanggal_kumpul, status)')
erd.node('Nilai', 'Nilai\n(id_nilai, id_pengumpulan, id_guru, skor, feedback)')
erd.node('Pengumuman', 'Pengumuman\n(id_pengumuman, id_kelas, id_admin, id_guru, isi_pengumuman, tanggal)')

# Relasi antara entitas
erd.edge('User', 'Kelas', label='1 : M (Guru Mengajar Kelas)')
erd.edge('User', 'Kelas_Murid', label='M : M (Murid Bergabung Kelas)')
erd.edge('Kelas', 'Tugas', label='1 : M (Kelas Punya Tugas)')
erd.edge('User', 'Tugas', label='1 : M (Guru Membuat Tugas)')
erd.edge('User', 'Pengumpulan_Tugas', label='1 : M (Murid Mengumpulkan Tugas)')
erd.edge('Tugas', 'Pengumpulan_Tugas', label='1 : M (Tugas Dikumpulkan)')
erd.edge('User', 'Nilai', label='1 : M (Guru Memberikan Nilai)')
erd.edge('Pengumpulan_Tugas', 'Nilai', label='1 : 1 (Tugas Dinilai)')
erd.edge('User', 'Pengumuman', label='1 : M (Admin/Guru Membuat Pengumuman)')
erd.edge('Kelas', 'Pengumuman', label='1 : M (Kelas Punya Pengumuman)')

# Menyimpan dan menampilkan ERD
erd_path = '/mnt/data/erd_murid_guru_admin.png'
erd.render(erd_path, format='png', cleanup=False)
erd_path
