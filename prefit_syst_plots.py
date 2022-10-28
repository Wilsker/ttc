import uproot
import matplotlib.pyplot as plt
import hist

def main():

    infile_ = '/afs/cern.ch/work/j/jthomasw/private/NTU/ExtraYukawa/ttc/workspace/CMSSW_10_2_13/src/HiggsAnalysis/LimitModel/FinalInputs/2018/ttc_a_rtu04_MA800/TMVApp_800_ee.root'

    try:
        tfile_ = uproot.open(infile_)
    except FileNotFoundError():
        raise FileNotFoundError( "Input file not {infile_} found" )

    process_name_ = 'Nonprompt'
    unc_name_ = 'fake'
    nom_file_name = 'ttc2018_'+process_name_
    up_file_name = 'ttc2018_'+process_name_+'_'+unc_name_+'Up'
    down_file_name = 'ttc2018_'+process_name_+'_'+unc_name_+'Down'

    fig, (ax1, ax2) = plt.subplots(2,1,gridspec_kw={'height_ratios':[2,1]})
    all_y = []
    all_x_lowedges=[]
    hnom_, nom_bin_edges_ = tfile_[nom_file_name].to_numpy()
    hup_, up_bin_edges_ = tfile_[up_file_name].to_numpy()
    hdown_, down_bin_edges_ = tfile_[down_file_name].to_numpy()

    all_y.append(hnom_)
    all_x_lowedges.append(nom_bin_edges_[:-1])
    all_y.append(hup_)
    all_x_lowedges.append(nom_bin_edges_[:-1])
    all_y.append(hdown_)
    all_x_lowedges.append(nom_bin_edges_[:-1])

    ns, bins, patches = ax1.hist(
    all_x_lowedges,
    nom_bin_edges_,
    weights=all_y,
    density=False,
    histtype='step',
    label=['nom', 'up', 'down'],
    )

    ax1.set_ylabel('entries')
    ax1.legend()


    ratio_nom_nom = hnom_/hnom_
    ratio_up_nom = hup_/hnom_
    ratio_down_nom = hdown_/hnom_

    all_ratio_y=[]
    all_ratio_x=[]

    all_ratio_y.append(ratio_nom_nom)
    all_ratio_y.append(ratio_up_nom)
    all_ratio_y.append(ratio_down_nom)
    all_ratio_x.append(nom_bin_edges_[:-1])
    all_ratio_x.append(nom_bin_edges_[:-1])
    all_ratio_x.append(nom_bin_edges_[:-1])


    ns, bins, patches = ax2.hist(
    all_x_lowedges,
    nom_bin_edges_,
    weights=all_ratio_y,
    density=False,
    histtype='step',
    label=['nom', 'up/nom', 'down/nom'],
    )

    #ax2.scatter()
    ax2.set_xlabel('BDT score')
    ax2.set_ylabel('unc./nom')

    save_file_name_ = 'prefit_'+nom_file_name+'_'+unc_name_+'plot.png'
    plt.savefig(save_file_name_)


    #print(fakes_fakeup_hist_)


if __name__ == '__main__':
    main()
