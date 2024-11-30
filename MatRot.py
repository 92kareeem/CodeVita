class MatRot:
    @staticmethod
    def main():
        ip = HndlrInp()
        sz_grd = ip.sz_rd_gd()
        grd_let = ip.ltr_mat_rd(sz_grd)
        cnt_qry = ip.rd_qry_cnt()

        hnd_query = ProcQry()
        for _ in range(cnt_qry):
            query_params = ip.para_rd_qry()
            hnd_query.rot_exec(grd_let, query_params[0], query_params[1], query_params[2])

        MatRot.mat_finl(grd_let)

    @staticmethod
    def mat_finl(letter_matrix):
        bldr_op = []
        for row in letter_matrix:
            bldr_op.extend(row)
        print(''.join(bldr_op))

class ProcQry:
    def rot_exec(self, mat, bsr, bsc, sbm_size):
        deplyr = sbm_size // 2
        for lay_curnt in range(deplyr):
            self.rot_layr(mat, bsr, bsc, sbm_size, lay_curnt)

    def rot_layr(self, mat, bsr, bsc, sbm_size, layr):
        ele_bod = self.bd_elexc(mat, bsr, bsc, sbm_size, layr)
        fact_rot = layr + 1
        ele_trnf = self.seqele_trsfm(ele_bod, fact_rot)
        self.mat_bd_upd(mat, bsr, bsc, sbm_size, layr, ele_trnf)

    def bd_elexc(self, mat, bsr, bsc, sz, layr):
        elmnts = []
        rw_st = bsr + layr
        rw_ed = bsr + sz - 1 - layr
        cl_strt = bsc + layr
        cl_ed = bsc + sz - 1 - layr
        for i in range(cl_strt,cl_ed + 1):
            elmnts.append(mat[rw_st][i])

        for i in range(rw_st + 1, rw_ed):
            elmnts.append(mat[i][cl_ed])

        for i in range(cl_ed, cl_strt - 1, -1):
            elmnts.append(mat[rw_ed][i])

        for i in range(rw_ed - 1, rw_st, -1):
            elmnts.append(mat[i][cl_strt])
        return elmnts

    def seqele_trsfm(self, sqnc, ind_rot):
        rot_effect = ind_rot % len(sqnc)
        if ind_rot % 2 == 1:
            sqnc = sqnc[rot_effect:] + sqnc[:rot_effect]
            return [self.ltr_shftbwd(symbol) for symbol in sqnc]
        else:
            sqnc = sqnc[-rot_effect:] + sqnc[:-rot_effect]
            return [self.ltr_shftfwd(symbol) for symbol in sqnc]

    def mat_bd_upd(self, mat, bsr, bsc, sz, layr, ele_trnf):
        rw_st = bsr + layr
        rw_ed = bsr + sz - 1 - layr
        cl_strt = bsc + layr
        cl_ed = bsc + sz - 1 - layr
        indx_ele = 0

        for i in range(cl_strt, cl_ed + 1):
            mat[rw_st][i] = ele_trnf[indx_ele]
            indx_ele += 1

        for i in range(rw_st + 1, rw_ed):
            mat[i][cl_ed] = ele_trnf[indx_ele]
            indx_ele += 1

        for i in range(cl_ed, cl_strt - 1, -1):
            mat[rw_ed][i] = ele_trnf[indx_ele]
            indx_ele += 1

        for i in range(rw_ed - 1, rw_st, -1):
            mat[i][cl_strt] = ele_trnf[indx_ele]
            indx_ele += 1

    def ltr_shftbwd(self, smbl):
        return 'Z' if smbl == 'A' else chr(ord(smbl) - 1)

    def ltr_shftfwd(self, symbl):
        return 'A' if symbl == 'Z' else chr(ord(symbl) + 1)
    
class HndlrInp:
    def sz_rd_gd(self):
        return int(input().strip())

    def ltr_mat_rd(self, sz_grd):
        mat_let = []
        for _ in range(sz_grd):
            ele_rw = input().strip().split()
            mat_let.append([char for char in ele_rw])
        return mat_let

    def rd_qry_cnt(self):
        return int(input().strip())

    def para_rd_qry(self):
        det_qry = input().strip().split()
        return [int(x) for x in det_qry]

if __name__ == '__main__':
    MatRot.main()
