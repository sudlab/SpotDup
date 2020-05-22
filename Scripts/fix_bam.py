import pysam
from collections import defaultdict
from cgatcore import experiment as E

def main():
    parser = E.ArgumentParser()    
    (options, args) = E.start(parser, unknowns=True)
    bamfile = pysam.AlignmentFile(args[0])
    outbam = pysam.AlignmentFile(args[1], "wb", template=bamfile)

    chunks=0
    
    for read1s, read2s in chunk_bam_by_readname(bamfile):
        chunks += 1
        if chunks % 1000000 == 0:
            E.info("Done %s fragments" % chunks)
            
        for contig in read1s:
            for read in read1s[contig]:
                read2 = find_read2(read2s, read)
                if read2 is not None:
                    outbam.write(read)
                    outbam.write(read2)

    outbam.close()
    E.stop()

def chunk_bam_by_readname(bamfile):

    read1_out = defaultdict(list)
    read2_out = defaultdict(list)
    current_readname = None
    
    for read in bamfile.fetch(until_eof=True):
        if not read.query_name == current_readname:
            yield (read1_out, read2_out)
            read1_out = defaultdict(list)
            read2_out = defaultdict(list)
            current_readname = read.query_name

        if read.is_read1:
            read1_out[read.reference_id].append(read)
        elif read.is_read2:
            read2_out[read.reference_id].append(read)
        else:
            raise ValueError("Read not read 1 or 2")

    yield (read1_out, read2_out)

def find_read2(read2s, read1):
    contig = read1.reference_id
    contig_read2s = read2s[contig]

    for read2 in contig_read2s:

        if read2.pos == read1.next_reference_start:
            read2.next_reference_start = read1.pos
            read2.template_length=-1*read1.template_length
                
            return read2
        
    return None

if __name__=="__main__":
    main()
