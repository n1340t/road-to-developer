# Data Structures That Power your Database
## Hash Indexes
## SSTables and LSM-Trees
> Log structure Indexing - index theo log
### Constructing and maintaining SSTables
Memtable là balanced tree data structure trên memory. Example: AVL tree hoặc red-black tree 
SSTables là data structure của memtable lưu trên disk
Nhược điểm nhỏ của memtable: bởi vì memtable được lưu ở trong memory nên khi database gặp sự cố (crash, etc.) thì có luồn ghi gần đây nhất (recent write) sẽ bị mất. Giải pháp là sử dụng một log riêng trên disk để lưu lại lịch sử của luồn ghi. 
### Making an LSM-tree out of SSTables
LevelDB and RocksDB là plugable storage engine? 
Indexing Structure sử dụng SSTables và memtables được gọi là **Log-Structured Merge-Tree (LSM-Tree)**. Storage engines sử dụng kỹ thuật merging and compacting sorted files được gọi là **LSM storage engines**. 
Lucene (indexing engine) used by Elasticsearch and Solr sử dụng ý tưởng tương tự để lưu "dictionary"
### Performance optimizations
Điều gì xảy ra khi tìm kiếm một key không có trong database? Thuật toán LSM-tree có thể bị chậm vì phải tìm kiếm trong memtable trước rồi tìm trong segment mới nhất cho tới cũ nhất. Tình huống xuất nhất là có thể đọc trong disk để chắc chắn rằng key không tồn tại.
Vấn đề/bài toán: Liệu có cách nào giúp chúng ta kiểm tra nhanh xem một element có nằm trong 1 set hay không? 
Giải pháp: Bloom Filter hoặc sketch algorithm?
Phương pháp tối ưu khác? Tìm thứ tự (order) và thời gian (timing) khi nào SSTables cần được compacted và merged. 2 cách phổ biến là size-tiered và leveled compaction. LevelDB và RocksDB sử dụng leveled compaction. HBase thì sử dụng size-tired. Cassandra thì hỗ trợ cả 2
Size-tired compaction: newer and smaller SSTables được merge thành older and larger SSTable
Leveled compaction: key range được chia thành smaller SSTable và data thì đưa qua "level" riêng biệt. Điều này cho phép quá trình compaction hoạt động incrementally và ít sử dụng diskspace hơn? (Cần tìm hiểu thêm)
Tóm tắt: LSM-tree giải quyết được bài toán data quá lớn không thể chứa hết trong memory. LSM-tree xử lý range queries hiệu quả hơn vì data (key) đã được sorted. LSM-tree supports high write throughput bởi vì disk writes are sequential (ghi theo thứ tự) not random.
## B-Trees
> ubiquitous - ở đâu cũng có, có mặt khắp mọi nơi

B-trees breaks database into pages or blocks (4KB in size). Mean while LSM breaks database into segment (several megabytes)
### Making B-tree reliable
Write in B-tree là overwrite page (modify file in place). Đôi khi chúng ta cần phải write cùng lúc nhiều pages (split page sau khi insertion làm cho nó full và phải update reference ở parent page). Đây là hành động nguy hiểm vì khi database crashes giữa chừng quá trình write, chúng ta sẽ bị corrupted index.
Giải pháp: Tương tự như LSM-Trees, chúng ta sẽ sử dụng log (write-ahead log - WAL or redo log) để dựng lại lịch sử write của database.
Vấn đề 2: concurrency writes (in place update)
Giải pháp: latches (lightweight locks)
Log-structured approaches giải quyết vấn đề này đơn giản hơn vì quá trình merging không can thiệp vào luồng writes
### B-tree optimizations
Có rất nhiều phương pháp tối ưu cho B-tree được phát triển qua nhiều năm.
- copy-on-write scheme (in LMDB database)  Tìm hiểu thêm?
- abbreviating key
- Use additional pointers
- Fractal trees
## Comparing B-Trees and LSM-Trees
> Rule of thumb, LSM tree write nhanh hơn. B-Tree đọc nhanh hơn

### Advantages of LSM-Trees
B-Tree bắt buộc phải write data ít nhất 2 lần. 1 lần ở page 1 lần ở log
*Write amplification* là 1 write lại sản sinh ra nhiều writes khác nhau. Cả 2 LSM and B-Tree đều có write amplification.
LSM Tree thường có write throughtput tốt hơn B-tree vì theo thiết kế write là sequential vào compact SSTable files hơn là overwrite nhiều pages.
LSM Tree compress tốt hơn và not page-oriented => Smaller files on disk
Key point: **log-structured algorithm can turn random writes into sequential**
### Downsides of LSM-Tree
Compaction can affect ongoing read and write process bởi vì disk có tài nguyên giới hạn
Problem: compaction không thể bắt kịp tốc độ ghi
Consequence: number of segments on disk keeps  growing until run out of space | read also slown down
Advantage of B-tree: index appears only once. => good for strong transactional semantics

Conclusion: B-tree vs LSM-Tree: Tired
## Other Indexing Structures

