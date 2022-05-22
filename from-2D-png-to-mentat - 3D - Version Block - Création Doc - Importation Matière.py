import time 
import re
from PIL import Image
import os
def main():
    namedoc=input("le nom du dossier :")
    startTime=time.time()
    for NuanceVariable in (0,255):
        NbImage=2
        for MousseVariable in range (0,NbImage):
            with Image.open("C:\\Users\\quent\\Desktop\\stage-thermo-m1\\Patin-Feutre-Rose-@10um\\1000x1000\Binaire\\Coupe_%03d.png"%(MousseVariable,), 'r') as image:
                if not os.path.exists('C:/Users/quent/Desktop/stage-thermo-m1/b-from-2d-png-to-mentat/' + namedoc +'/Nuance-%d/img-%d/'%(NuanceVariable, MousseVariable)):
                    os.makedirs('C:/Users/quent/Desktop/stage-thermo-m1/b-from-2d-png-to-mentat/' + namedoc +'/Nuance-%d/img-%d/'%(NuanceVariable, MousseVariable))
                block=1;
                (imglength,imgheight)=image.size;
                array_1 = [];
                for i in range(0, imgheight):
                    a = [];
                    for j in range(0, imglength):
                        a.append(int(0));
                        array_1.append(a);
                name0="mesh-for-mentat-check_job%d.txt"%(MousseVariable);
                fout0 = open('C:\\Users\\quent\\Desktop\\stage-thermo-m1\\b-from-2d-png-to-mentat\\' + namedoc + '\\Nuance-%d\\img-%d\\'%(NuanceVariable, MousseVariable) + name0,'w');
                atoid=0; mesh_x=list(); mesh_y=list(); mesh_z=list()
                zVar=MousseVariable+1
                for z in range(MousseVariable,zVar):
                    for y in range(0, imgheight):
                        for x in range(0, imglength):
                            colorcode_ref = NuanceVariable; coordinate=x,y;
                            array_1[y][x]=image.getpixel(coordinate); colorcode=array_1[y][x];
                            if colorcode == colorcode_ref:
                                atoid=atoid+8;
                                x_new_1=x;   y_new_1=imgheight-y; z_new_1=z; mesh_x.append(x_new_1); mesh_y.append(y_new_1); mesh_z.append(z_new_1);
                                x_new_2=x+1; y_new_2=y_new_1; z_new_2=z;     mesh_x.append(x_new_2); mesh_y.append(y_new_2); mesh_z.append(z_new_2);
                                x_new_3=x+1; y_new_3=y_new_1+1; z_new_3=z;   mesh_x.append(x_new_3); mesh_y.append(y_new_3); mesh_z.append(z_new_3);
                                x_new_4=x;   y_new_4=y_new_1+1; z_new_4=z;   mesh_x.append(x_new_4); mesh_y.append(y_new_4); mesh_z.append(z_new_4);
                                x_new_5=x;   y_new_5=imgheight-y; z_new_5=z+1; mesh_x.append(x_new_5); mesh_y.append(y_new_5); mesh_z.append(z_new_5);
                                x_new_6=x+1; y_new_6=y_new_1; z_new_6=z+1;     mesh_x.append(x_new_6); mesh_y.append(y_new_6); mesh_z.append(z_new_6);
                                x_new_7=x+1; y_new_7=y_new_1+1; z_new_7=z+1;   mesh_x.append(x_new_7); mesh_y.append(y_new_7); mesh_z.append(z_new_7);
                                x_new_8=x;   y_new_8=y_new_1+1; z_new_8=z+1;   mesh_x.append(x_new_8); mesh_y.append(y_new_8); mesh_z.append(z_new_8);
                                fout0.write("pixel(x;y) ; color -> %f %f %f %d %d \n" % (x,y,z,array_1[y][x],atoid));        
                print("fin de nuance %d img %d"%(NuanceVariable,MousseVariable)); image.close(); fout0.close();
                otfy1=(int(float(atoid)/8.0))+1; 
                nbgro=(int(float(otfy1)/(float(block+1)-1.0)))+1; 
                d_snap=8*nbgro; 
                drag1=0; 
                for snap1 in range(1, (block+1)):
                    name1="mesh-for-mentat-snap-%d_job%d.dat" % (snap1,MousseVariable);
                    fout1 = open('C:\\Users\\quent\\Desktop\\stage-thermo-m1\\b-from-2d-png-to-mentat\\' + namedoc + '\\Nuance-%d\\img-%d\\'%(NuanceVariable, MousseVariable) + name1,'w');
                    fout1.write("title               job1 \n");
                    fout1.write("$....MARC input file produced by Marc Mentat 2021.1 (64bit) Student Edition \n");
                    fout1.write("$................................... \n");
                    fout1.write("$....input file using extended precision \n");
                    fout1.write("extended \n");
                    fout1.write("$................................... \n");
                    fout1.write("sizing                                 0         8        27         0 \n");
                    fout1.write("alloc                       25 \n");
                    fout1.write("elements                     7 \n");
                    fout1.write("version                     15         2         0         0 \n");
                    fout1.write("table                        0         0         2         1         1         0         0         1 \n");
                    fout1.write("processor                    1         1         1         0 \n");
                    fout1.write("$no list \n");
                    fout1.write("large stra                   4       213       123       130       230       123         1         0 \n");
                    fout1.write("all points \n");
                    fout1.write("no echo                      1         2         3         4 \n");
                    #fout1.write("shell sect                   5         0         1 \n");
                    fout1.write("end \n");
                    fout1.write("$................... \n");
                    fout1.write("solver \n");
                    fout1.write("         8         0         0         0         0         0         0         0         0         0         0         0         0         0         0         0 \n");
                    fout1.write("optimize                    11 \n");
                    fout1.write("connectivity \n");
                    fout1.write("%10d%10d%10d%10d%10d%10d%10d%10d%10d\n" % (0,0,1,0,0,0,0,0,1));                    
                    borne_inf=(snap1-1)*d_snap;
                    borne_sup=(snap1*d_snap);
                    if borne_sup > atoid:
                        borne_sup=atoid; drag1=1;
                    nbgro=int(float(borne_sup-borne_inf+1)/8.0);
                    cnt=0;
                    for i in range(0, nbgro):
                        cnt=cnt+1;
                        i1=8*(cnt-1)+1+borne_inf; 
                        i2=8*(cnt-1)+2+borne_inf;
                        i3=8*(cnt-1)+3+borne_inf;
                        i4=8*(cnt-1)+4+borne_inf;
                        i5=8*(cnt-1)+5+borne_inf; 
                        i6=8*(cnt-1)+6+borne_inf;
                        i7=8*(cnt-1)+7+borne_inf;
                        i8=8*(cnt-1)+8+borne_inf;
                        fout1.write("%10d%10d%10d%10d%10d%10d%10d%10d%10d%10d\n" % (((snap1-1)*nbgro+cnt),7,i1,i2,i3,i4,i5,i6,i7,i8));
                    fout1.write("coordinates \n");
                    fout1.write("%10d%10d%10d%10d\n" % (3,cnt,0,1));
                    cnt=0;
                    for i in range(borne_inf,borne_sup):
                        cnt=cnt+1;
                        digitx="%0.15e" % (mesh_x[i]); new_digitx=re.sub(r"e\+0","+",digitx);
                        digity="%0.15e" % (mesh_y[i]); new_digity=re.sub(r"e\+0","+",digity);
                        digitz="%0.15e" % (mesh_z[i]); new_digitz=re.sub(r"e\+0","+",digitz);
                        fout1.write("%10d %s %s %s\n" % ((borne_inf+cnt),new_digitx,new_digity,new_digitz));    
                    fout1.write("loadcase            job1 \n");
                    fout1.write("         0 \n");
                    fout1.write("no print \n");
                    fout1.write("post \n");
                    fout1.write("        0        16        17         0         0        19        20         0         1         0         0         0         0         0         0         0 \n");
                    fout1.write("parameters \n");
                    fout1.write(" 1.000000000000000+0 1.000000000000000+9 1.000000000000000+2 1.000000000000000+6 2.500000000000000-1 5.000000000000000-1 1.500000000000000+0-5.000000000000000-1 \n");
                    fout1.write(" 8.625000000000000+0 2.000000000000000+1 1.000000000000000-4 1.000000000000000-6 1.000000000000000+0 1.000000000000000-4 \n");
                    fout1.write(" 8.314000000000000+0 2.731500000000000+2 5.000000000000000-1 0.000000000000000+0 5.670510000000000-8 1.438769000000000-2 2.997900000000000+8 1.00000000000000+30 \n");
                    fout1.write(" 0.000000000000000+0 0.000000000000000+0 1.000000000000000+2 0.000000000000000+0 1.000000000000000+0-2.000000000000000+0 1.000000000000000+6 3.000000000000000+0 \n");
                    fout1.write(" 0.000000000000000+0 0.000000000000000+0 1.256637061000000-6 8.85418781700000-12 1.200000000000000+2 1.000000000000000-3 1.600000000000000+2 0.000000000000000+0 \n");
                    fout1.write(" 3.000000000000000+0 4.000000000000000-1 \n");
                    fout1.write("end option \n");
                    fout1.write("$................... \n");
                    fout1.close();
                    if drag1 == 1:
                        break;
        if NuanceVariable==0:
            mass=("1140");
            conduc=("0.23");
            spec_heat=("1.5e+06");
        else:
            mass=("1");
            conduc=("0.025");
            spec_heat=("1004");
        name2="mymentat-to-run-Nuance%d.proc"%(NuanceVariable);
        fout2 = open('C:\\Users\\quent\\Desktop\\stage-thermo-m1\\b-from-2d-png-to-mentat\\' + namedoc + '\\' + name2, 'w');
        fout2.write("| Created by Marc Mentat 2021.3.1 (64bit)\n");
        fout2.write("*prog_option compatibility:prog_version:ment2021.3\n");
        fout2.write("*prog_use_current_job off\n")
        fout2.write("*prog_analysis_class thermal\n")
        fout2.write("*set_default_length_unit millimeter\n");
        fout2.write("*set_model_length_unit millimeter\n");
        fout2.write("|\n");
        for MousseVariable in range(0,NbImage):
            for snap1 in range (1,(block+1)):
                fout2.write("*import marc_read \"Nuance-%d\img-%d\mesh-for-mentat-snap-%d_job%d.dat\"\n" % (NuanceVariable,MousseVariable,snap1,MousseVariable));
                fout2.write("*reset_view\n");
                fout2.write("*fill_view\n");
                fout2.write("*set_save_formatted off\n");
                fout2.write("*save_as_model \"modelenuance%d.mud\" yes\n"%(NuanceVariable));
        fout2.write("*sweep_nodes\n");
        fout2.write("all_existing\n");
        fout2.write("*sweep_elements\n");
        fout2.write("all_existing\n");
        fout2.write("*prog_use_current_job off\n");
        fout2.write("*prog_analysis_class thermal\n");
        fout2.write("*new_mater standard\n");
        fout2.write("*mater_param general:mass_density %s\n"%(mass));
        fout2.write("*mater_param thermal:conductivity %s\n"%(conduc));
        fout2.write("mater_param thermal:specific_heat %s\n"%(spec_heat));
        fout2.write("*save_as_model \"modelenuance%d.mud\" yes\n"%(NuanceVariable));
        fout2.write("*add_mater_elements\n");
        fout2.write("all_existing\n");
        fout2.write("*edit_job job1 *remove_current_job\n");
        for supjob in range(1,NbImage):
            fout2.write("*edit_job job1_%d *remove_current_job\n"%(supjob)); 
        fout2.write("*new_job thermal\n")
        fout2.write("*edit_job job1\n")
        fout2.write("*update_job\n")
        fout2.write("*job_write_input\n")
        fout2.write("yes\n")
        fout2.write("*save_model *quit yes\n");
    name3="mymentat-to-run-assembly.proc"
    fout3 = open('C:\\Users\\quent\\Desktop\\stage-thermo-m1\\b-from-2d-png-to-mentat\\' + namedoc + '\\' + name3, 'w');
    fout3.write("| Created by Marc Mentat 2021.3.1 (64bit)\n");
    fout3.write("*prog_option compatibility:prog_version:ment2021.3\n");
    fout3.write("*prog_use_current_job off\n");
    fout3.write("*prog_analysis_class thermal\n");
    fout3.write("*set_default_length_unit millimeter\n");
    fout3.write("*set_model_length_unit millimeter\n");
    fout3.write("|\n");
    fout3.write("*import marc_read \"modelenuance0_job1.dat\"\n");
    fout3.write("*import marc_read \"modelenuance255_job1.dat\"\n");
    fout3.write("*edit_mater material1\n");
    fout3.write("*mater_color\n");
    fout3.write("0 85 255\n");
    fout2.write("*save_as_model \"modeleassembly.mud\" yes\n");
    fout3.write("*save_model *quit yes\n");
    executionTime=(time.time()-startTime)
    print('Execution time in seconds: '+str(executionTime))
if __name__ == '__main__':
    main();