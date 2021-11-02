from Bio import SeqIO
for seq_record in SeqIO.parse("RBD_fasta.fasta", "fasta"):
	print(seq_record.id)
	print(repr(seq_record.seq))
	print(len(seq_record))
# aa pos-319=mettere in quadra
	print(seq_record[501-319])

# for mutation:
	from Bio.Seq import MutableSeq
	mutable_seq = MutableSeq(seq_record.seq)
	mutable_seq[501-319] = "Y"
	print(mutable_seq[501-319])

	from Bio.Seq import Seq
	from Bio.SeqRecord import SeqRecord
	record1 = SeqRecord(
		Seq(
			mutable_seq
		),
		id="alpha_variant|RBD",
		description="Sars-Cov-2",
	)
	print(record1.format("fasta"))

# variant_gamma
	mutable_seq_gamma = MutableSeq(seq_record.seq)
	mutable_seq_gamma[417-319] = "T"
	mutable_seq_gamma[484-319] = "K"
	mutable_seq_gamma[501-319] = "Y"
	print(mutable_seq_gamma[484-319])

	record2 = SeqRecord(
		Seq(
			mutable_seq_gamma
		),
		id="gamma_variant|RBD",
		description="Sars-Cov-2",
	)
	print(record2.format("fasta"))

my_records = [record1, record2]
SeqIO.write(my_records, "RBD_variant.fasta", "fasta")
