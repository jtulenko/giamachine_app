import datetime
import pymysql

import common
import plotting


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/lab')
def lab():


    dbc = common.reader_connect_to_db()
    dbcursor = dbc.cursor()
    query1 = """select distinct _be10_al26_quartz.chem_lab
        from _be10_al26_quartz
        where _be10_al26_quartz.chem_lab is not null
        and _be10_al26_quartz.chem_lab != ""
        order by _be10_al26_quartz.chem_lab """
    dbcursor.execute(query1)
    result = dbcursor.fetchall()
    n1 = len(result)
    s1 = []
    for item in result:
        this_link = '<a href="be10al26/' + item[0] + '" target="_blank">' + item[0] + '</a>'
        s1.append(this_link)


    query2 = """select distinct _he3_pxol.system
       from _he3_pxol
       where _he3_pxol.system is not null
       and _he3_pxol.system != ""
       order by _he3_pxol.system"""
    dbcursor.execute(query2)
    result = dbcursor.fetchall()
    n2 = len(result)
    s2 = []
    for item in result:
        this_link = '<a href="he3pxol/' + item[0] + '" target="_blank">' + item[0] + '</a>'
        s2.append(this_link)


    query3 = """select distinct _cl36.chem_lab
        from _cl36
        where _cl36.chem_lab is not null
        and _cl36.chem_lab != ""
        order by _cl36.chem_lab """
    dbcursor.execute(query3)
    result = dbcursor.fetchall()
    n3 = len(result)
    s3 = []
    for item in result:
        this_link = '<a href="cl36/' + item[0] + '" target="_blank">' + item[0] + '</a>'
        s3.append(this_link)


    query4 = """select distinct _he3_quartz.system
       from _he3_quartz
       where _he3_quartz.system is not null
       and _he3_quartz.system != ""
       order by _he3_quartz.system"""
    dbcursor.execute(query4)
    result = dbcursor.fetchall()
    n4 = len(result)
    s4 = []
    for item in result:
        this_link = '<a href="he3qtz/' + item[0] + '" target="_blank">' + item[0] + '</a>'
        s4.append(this_link)


    query5 = """select distinct _c14_quartz.extraction_lab
       from _c14_quartz
       where _c14_quartz.extraction_lab is not null
       and _c14_quartz.extraction_lab != ""
       order by _c14_quartz.extraction_lab"""
    dbcursor.execute(query5)
    result = dbcursor.fetchall()
    n5 = len(result)
    s5 = []
    for item in result:
        this_link = '<a href="c14/' + item[0] + '" target="_blank">' + item[0] + '</a>'
        s5.append(this_link)


    query6 = """select distinct _ne21_quartz.system
       from _ne21_quartz
       where _ne21_quartz.system is not null
       and _ne21_quartz.system != ""
       order by _ne21_quartz.system"""
    dbcursor.execute(query6)
    result = dbcursor.fetchall()
    n6 = len(result)
    s6 = []
    for item in result:
        this_link = '<a href="ne21/' + item[0] + '" target="_blank">' + item[0] + '</a>'
        s6.append(this_link)

    queryplot1 = """select iced._be10_al26_quartz.N10_atoms_g, iced._be10_al26_quartz.delN10_atoms_g, iced.base_sample.name, iced._be10_al26_quartz.chem_lab
        from iced._be10_al26_quartz, iced.base_sample
        where iced.base_sample.id = iced._be10_al26_quartz.sample_id
        and iced._be10_al26_quartz.N10_atoms_g is not null
        and iced._be10_al26_quartz.delN10_atoms_g is not null
        and iced._be10_al26_quartz.N10_atoms_g  != 0
        and iced._be10_al26_quartz.delN10_atoms_g  != 0"""
    dbcursor.execute(queryplot1)
    r1 = dbcursor.fetchall()
    l1 = len(r1)
    [script1,div1] = plotting.be_plot(r1)

    queryplot2 = """select iced._be10_al26_quartz.N26_atoms_g, iced._be10_al26_quartz.delN26_atoms_g, iced.base_sample.name, iced._be10_al26_quartz.chem_lab
        from iced._be10_al26_quartz, iced.base_sample
        where iced.base_sample.id = iced._be10_al26_quartz.sample_id
        and iced._be10_al26_quartz.N26_atoms_g is not null
        and iced._be10_al26_quartz.delN26_atoms_g is not null
        and iced._be10_al26_quartz.N26_atoms_g  != 0
        and iced._be10_al26_quartz.delN26_atoms_g  != 0"""
    dbcursor.execute(queryplot2)
    r2 = dbcursor.fetchall()
    l2 = len(r2)
    [script2,div2] = plotting.al_plot(r2)

    queryplot3 = """select iced._c14_quartz.N14_atoms_g, iced._c14_quartz.delN14_atoms_g, iced.base_sample.name, iced._c14_quartz.extraction_lab
        from iced._c14_quartz, iced.base_sample
        where iced.base_sample.id = iced._c14_quartz.sample_id
        and iced._c14_quartz.N14_atoms_g is not null
        and iced._c14_quartz.delN14_atoms_g is not null
        and iced._c14_quartz.N14_atoms_g  != 0
        and iced._c14_quartz.delN14_atoms_g  != 0"""
    dbcursor.execute(queryplot3)
    r3 = dbcursor.fetchall()
    l3 = len(r3)
    [script3,div3] = plotting.c_plot(r3)

    queryplot4 = """select iced._he3_pxol.N3c_atoms_g, iced._he3_pxol.delN3c_atoms_g, iced.base_sample.name, iced._he3_pxol.system
        from iced._he3_pxol, iced.base_sample
        where iced.base_sample.id = iced._he3_pxol.id
        and iced._he3_pxol.N3c_atoms_g is not null
        and iced._he3_pxol.delN3c_atoms_g is not null
        and iced._he3_pxol.N3c_atoms_g  != 0
        and iced._he3_pxol.delN3c_atoms_g  != 0"""
    dbcursor.execute(queryplot4)
    r4 = dbcursor.fetchall()
    l4 = len(r4)
    [script4,div4] = plotting.hepxol_plot(r4)

    queryplot5 = """select _he3_quartz.N3c_atoms_g, _he3_quartz.delN3c_atoms_g, iced.base_sample.name, _he3_quartz.system
        from _he3_quartz, iced.base_sample
        where iced.base_sample.id = _he3_quartz.sample_id
        and _he3_quartz.N3c_atoms_g is not null
        and _he3_quartz.delN3c_atoms_g is not null
        and _he3_quartz.N3c_atoms_g != 0
        and _he3_quartz.delN3c_atoms_g != 0"""
    dbcursor.execute(queryplot5)
    r5 = dbcursor.fetchall()
    l5 = len(r5)
    [script5,div5] = plotting.heqtz_plot(r5)

    queryplot6 = """select _cl36.N36_atoms_g, base_calculatedage.t_st, base_calculatedage.dtint_st, iced.base_sample.name, _cl36.chem_lab
        from _cl36, base_calculatedage, iced.base_sample
        where _cl36.sample_id = base_calculatedage.sample_id
        and iced.base_sample.id = _cl36.sample_id
        and base_calculatedage.nuclide like 't36'"""
    dbcursor.execute(queryplot6)
    r6 = dbcursor.fetchall()
    l6 = len(r6)
    [script6,div6] = plotting.cl_plot(r6)


    queryplot7 = """select _ne21_quartz.N21xs_atoms_g, _ne21_quartz.delN21xs_atoms_g, iced.base_sample.name, _ne21_quartz.system
        from _ne21_quartz, iced.base_sample
        where iced.base_sample.id = iced._ne21_quartz.sample_id
        and _ne21_quartz.N21xs_atoms_g is not null
        and _ne21_quartz.delN21xs_atoms_g is not null
        and _ne21_quartz.N21xs_atoms_g != 0
        and _ne21_quartz.delN21xs_atoms_g != 0"""
    dbcursor.execute(queryplot7)
    r7 = dbcursor.fetchall()
    l7 = len(r7)
    [script7,div7] = plotting.ne_plot(r7)

    dbc.close()

    return render_template('iced_lab.html', beal=s1, n1=n1, hepxol=s2, n2=n2, cl=s3, n3=n3, heqtz=s4, n4=n4, carbon=s5, n5=n5, neon=s6, n6=n6, be_script=script1, be_div=div1, l1=l1, al_script=script2, al_div=div2, l2=l2, c_script=script3, c_div=div3, l3=l3, he1_script=script4, he1_div=div4, l4=l4, he2_script=script5, he2_div=div5, l5=l5, cl_script=script6, cl_div=div6, l6=l6, ne_script=script7, ne_div=div7, l7=l7)


@app.route('/be10al26/<labname>')
def beal(labname):



    dbc = common.reader_connect_to_db()
    dbcursor = dbc.cursor()

    dbcursor.execute('select distinct chem_lab from _be10_al26_quartz')
    existing_labs = dbcursor.fetchall()
    lab_exists = False
    for lab in existing_labs:
        if labname in lab:
            lab_exists = True

    if lab_exists:

        q1 = """select base_sample.name, base_application.name
            from base_sample, _be10_al26_quartz, base_site, base_application_sites, base_application
            where base_sample.id = _be10_al26_quartz.sample_id
            and base_sample.site_id = base_site.id
            and base_site.id = base_application_sites.site_id
            and base_application_sites.application_id = base_application.id
            and _be10_al26_quartz.chem_lab = 'XXXX'
            order by base_sample.name"""
        q1 = q1.replace('XXXX',labname)
        dbcursor.execute(q1)
        result = dbcursor.fetchall()

        q2 = "select _be10_al26_quartz.N10_atoms_g,_be10_al26_quartz.delN10_atoms_g, iced.base_sample.name, iced._be10_al26_quartz.chem_lab from _be10_al26_quartz, iced.base_sample where chem_lab = '" + labname + "' and iced.base_sample.id = iced._be10_al26_quartz.sample_id"
        dbcursor.execute(q2)
        r2 = dbcursor.fetchall()

        q3 = """select iced._be10_al26_quartz.N10_atoms_g, iced._be10_al26_quartz.delN10_atoms_g
            from iced._be10_al26_quartz
            where iced._be10_al26_quartz.N10_atoms_g is not null
            and iced._be10_al26_quartz.delN10_atoms_g is not null
            and iced._be10_al26_quartz.N10_atoms_g  != 0
            and iced._be10_al26_quartz.chem_lab != 'XXXX'
            and iced._be10_al26_quartz.delN10_atoms_g  != 0"""
        q3 = q3.replace('XXXX', labname)
        dbcursor.execute(q3)
        r3 = dbcursor.fetchall()

        [plot_script,plot_div] = plotting.be_plot2(r2, r3)

        geo_q1 = "select iced.base_sample.lat_DD, iced.base_sample.lon_DD, iced.base_sample.name from _be10_al26_quartz, iced.base_sample where chem_lab = '" + labname + "' and iced.base_sample.id = iced._be10_al26_quartz.sample_id"
        dbcursor.execute(geo_q1)
        geo_r1 = dbcursor.fetchall()

        [plot_script1_geo,plot_div1_geo] = plotting.geo_map(geo_r1)

        q4 = "select _be10_al26_quartz.N26_atoms_g, _be10_al26_quartz.delN26_atoms_g, iced.base_sample.name, iced._be10_al26_quartz.chem_lab from _be10_al26_quartz, iced.base_sample where _be10_al26_quartz.chem_lab = '" + labname + "' and iced.base_sample.id = iced._be10_al26_quartz.sample_id and iced._be10_al26_quartz.N26_atoms_g is not null and iced._be10_al26_quartz.delN26_atoms_g is not null and iced._be10_al26_quartz.N26_atoms_g  != 0 and iced._be10_al26_quartz.delN26_atoms_g  != 0"
        dbcursor.execute(q4)
        r4 = dbcursor.fetchall()

        q5 = """select iced._be10_al26_quartz.N26_atoms_g, iced._be10_al26_quartz.delN26_atoms_g
            from iced._be10_al26_quartz
            where iced._be10_al26_quartz.N26_atoms_g is not null
            and iced._be10_al26_quartz.delN26_atoms_g is not null
            and iced._be10_al26_quartz.N26_atoms_g  != 0
            and iced._be10_al26_quartz.chem_lab != 'XXXX'
            and iced._be10_al26_quartz.delN26_atoms_g  != 0"""
        q5 = q5.replace('XXXX', labname)
        dbcursor.execute(q5)
        r5 = dbcursor.fetchall()

        if len(r4) == 0:
            plot_script2 = ''
            plot_div2 = ''

        else:
            [plot_script2,plot_div2] = plotting.al_plot2(r4, r5)

        n = len(result)
        s = []
        for item in result:
            this_link = '<a href="https://version2.ice-d.org/' + item[1] + '/sample/' + item[0] + '" target="_blank">' + item[0] + '</a>'
            s.append(this_link)

    else:
        s = 'No such lab'
        n = 0
        plot_script = ''
        plot_div = ''
        plot_script2 = ''
        plot_div2 = ''

    dbc.close()

    return render_template('be10al26.html', text=s, labname=labname, n=n, script=plot_script, div=plot_div, script1b=plot_script1_geo, div1b=plot_div1_geo, script2=plot_script2, div2=plot_div2)



@app.route('/he3pxol/<labname>')
def hepxol(labname):


    dbc = common.reader_connect_to_db()
    dbcursor = dbc.cursor()

    dbcursor.execute('select distinct _he3_pxol.system from _he3_pxol')
    existing_labs = dbcursor.fetchall()
    lab_exists = False
    for lab in existing_labs:
        if labname in lab:
            lab_exists = True

    if lab_exists:

        q1 = """select base_sample.name, base_application.name
            from base_sample, _he3_pxol, base_site, base_application_sites, base_application
            where base_sample.id = _he3_pxol.sample_id
            and base_sample.site_id = base_site.id
            and base_site.id = base_application_sites.site_id
            and base_application_sites.application_id = base_application.id
            and _he3_pxol.system = 'XXXX'
            order by base_sample.name """
        q1 = q1.replace('XXXX',labname)
        dbcursor.execute(q1)
        result = dbcursor.fetchall()

        q2 = "select _he3_pxol.N3c_atoms_g,_he3_pxol.delN3c_atoms_g, iced.base_sample.name, _he3_pxol.system from _he3_pxol, iced.base_sample where _he3_pxol.system = '" + labname + "' and iced.base_sample.id=_he3_pxol.sample_id"
        dbcursor.execute(q2)
        r2 = dbcursor.fetchall()

        q3 = """select iced._he3_pxol.N3c_atoms_g, iced._he3_pxol.delN3c_atoms_g
            from iced._he3_pxol
            where iced._he3_pxol.N3c_atoms_g is not null
            and iced._he3_pxol.delN3c_atoms_g is not null
            and iced._he3_pxol.N3c_atoms_g  != 0
            and iced._he3_pxol.system != 'XXXX'
            and iced._he3_pxol.delN3c_atoms_g  != 0"""
        q3 = q3.replace('XXXX', labname)
        dbcursor.execute(q3)
        r3 = dbcursor.fetchall()


        n = len(result)
        s = []
        for item in result:
            this_link = '<a href="https://version2.ice-d.org/' + item[1] + '/sample/' + item[0] + '" target="_blank">' + item[0] + '</a>'
            s.append(this_link)

        [plot_script,plot_div] = plotting.hepxol_plot2(r2, r3)

    else:
        s = 'No such lab'
        n = 0
        plot_script = ''
        plot_div = ''

    dbc.close()

    return render_template('he3pxol.html', text=s, labname=labname, n=n, script=plot_script, div=plot_div)


@app.route('/he3qtz/<labname>')
def heqtz(labname):


    dbc = common.reader_connect_to_db()
    dbcursor = dbc.cursor()

    dbcursor.execute('select distinct _he3_quartz.system from _he3_quartz')
    existing_labs = dbcursor.fetchall()
    lab_exists = False
    for lab in existing_labs:
        if labname in lab:
            lab_exists = True

    if lab_exists:

        q1 = """select base_sample.name, base_application.name
            from base_sample, _he3_quartz, base_site, base_application_sites, base_application
            where base_sample.id = _he3_quartz.sample_id
            and base_sample.site_id = base_site.id
            and base_site.id = base_application_sites.site_id
            and base_application_sites.application_id = base_application.id
            and _he3_quartz.system = 'XXXX'
            order by base_sample.name """
        q1 = q1.replace('XXXX',labname)
        dbcursor.execute(q1)
        result = dbcursor.fetchall()

        q2 = "select _he3_quartz.N3c_atoms_g,_he3_quartz.delN3c_atoms_g, iced.base_sample.name, _he3_quartz.system from _he3_quartz, iced.base_sample where _he3_quartz.system = '" + labname + "' and iced.base_sample.id = _he3_quartz.sample_id"
        dbcursor.execute(q2)
        r2 = dbcursor.fetchall()

        q3 = """select _he3_quartz.N3c_atoms_g, _he3_quartz.delN3c_atoms_g
            from _he3_quartz
            where _he3_quartz.N3c_atoms_g is not null
            and _he3_quartz.delN3c_atoms_g is not null
            and _he3_quartz.N3c_atoms_g != 0
            and _he3_quartz.system != 'XXXX'
            and _he3_quartz.delN3c_atoms_g != 0"""
        q3 = q3.replace('XXXX', labname)
        dbcursor.execute(q3)
        r3 = dbcursor.fetchall()

        n = len(result)
        s = []
        for item in result:
            this_link = '<a href="https://version2.ice-d.org/' + item[1] + '/sample/' + item[0] + '" target="_blank">' + item[0] + '</a>'
            s.append(this_link)

        [plot_script,plot_div] = plotting.heqtz_plot2(r2, r3)

    else:
        s = 'No such lab'
        n = 0
        plot_script = ''
        plot_div = ''

    dbc.close()

    return render_template('he3qtz.html', text=s, labname=labname, n=n, script=plot_script, div=plot_div)


@app.route('/ne21/<labname>')
def neon(labname):


    dbc = common.reader_connect_to_db()
    dbcursor = dbc.cursor()

    dbcursor.execute('select distinct _ne21_quartz.system from _ne21_quartz')
    existing_labs = dbcursor.fetchall()
    lab_exists = False
    for lab in existing_labs:
        if labname in lab:
            lab_exists = True

    if lab_exists:

        q1 = """select base_sample.name, base_application.name
            from base_sample, _ne21_quartz, base_site, base_application_sites, base_application
            where base_sample.id = _ne21_quartz.sample_id
            and base_sample.site_id = base_site.id
            and base_site.id = base_application_sites.site_id
            and base_application_sites.application_id = base_application.id
            and _ne21_quartz.system = 'XXXX'
            order by base_sample.name"""
        q1 = q1.replace('XXXX', labname)
        dbcursor.execute(q1)
        result = dbcursor.fetchall()

        q2 = "select _ne21_quartz.N21xs_atoms_g, _ne21_quartz.delN21xs_atoms_g, iced.base_sample.name, _ne21_quartz.system from _ne21_quartz, iced.base_sample where _ne21_quartz.system = '" + labname + "' and iced.base_sample.id = _ne21_quartz.sample_id"
        dbcursor.execute(q2)
        r2 = dbcursor.fetchall()

        q3 = """select iced._ne21_quartz.N21xs_atoms_g, iced._ne21_quartz.delN21xs_atoms_g
            from iced._ne21_quartz, iced.base_sample
            where iced.base_sample.id = iced._ne21_quartz.sample_id
            and iced._ne21_quartz.N21xs_atoms_g is not null
            and iced._ne21_quartz.delN21xs_atoms_g is not null
            and iced._ne21_quartz.N21xs_atoms_g != 0
            and iced._ne21_quartz.system != 'XXXX'
            and iced._ne21_quartz.delN21xs_atoms_g != 0"""
        q3 = q3.replace('XXXX', labname)
        dbcursor.execute(q3)
        r3 = dbcursor.fetchall()

        n = len(result)
        s = []
        for item in result:
            this_link = '<a href="https://version2.ice-d.org/' + item[1] + '/sample/' + item[0] + '" target="_blank">' + item[0] + '</a>'
            s.append(this_link)

        [plot_script, plot_div] = plotting.ne_plot2(r2,r3)

    else:
        s = 'No such lab'
        n = 0
        plot_script = ''
        plot_div = ''

    dbc.close()

    return render_template('ne21.html', text=s, labname=labname, n=n, script=plot_script, div=plot_div)


@app.route('/cl36/<labname>')
def cl(labname):


    dbc = common.reader_connect_to_db()
    dbcursor = dbc.cursor()

    dbcursor.execute('select distinct _cl36.chem_lab from _cl36')
    existing_labs = dbcursor.fetchall()
    lab_exists = False
    for lab in existing_labs:
        if labname in lab:
            lab_exists = True

    if lab_exists:

        q1 = """select base_sample.name, base_application.name
            from base_sample, _cl36, base_site, base_application_sites, base_application
            where base_sample.id = _cl36.sample_id
            and base_sample.site_id = base_site.id
            and base_site.id = base_application_sites.site_id
            and base_application_sites.application_id = base_application.id
            and _cl36.chem_lab = 'XXXX'
            order by base_sample.name"""
        q1 = q1.replace('XXXX',labname)
        dbcursor.execute(q1)
        result = dbcursor.fetchall()

        q2 = "select _cl36.N36_atoms_g,base_calculatedage.t_st,base_calculatedage.dtint_st, iced.base_sample.name, _cl36.chem_lab from _cl36, base_calculatedage, iced.base_sample where base_calculatedage.sample_id = _cl36.sample_id and iced.base_sample.id = _cl36.sample_id and base_calculatedage.Nuclide like 't36' and _cl36.chem_lab = '" + labname + "'"
        dbcursor.execute(q2)
        r2 = dbcursor.fetchall()


        q3 = """select _cl36.N36_atoms_g, base_calculatedage.t_st, base_calculatedage.dtint_st
            from _cl36, base_calculatedage
            where _cl36.sample_id = base_calculatedage.sample_id
            and _cl36.chem_lab != 'XXXX'
            and base_calculatedage.nuclide like 't36'"""
        q3 = q3.replace('XXXX', labname)
        dbcursor.execute(q3)
        r3 = dbcursor.fetchall()

        n = len(result)
        s = []
        for item in result:
            this_link = '<a href="https://version2.ice-d.org/' + item[1] + '/sample/' + item[0] + '" target="_blank">' + item[0] + '</a>'
            s.append(this_link)

        [plot_script,plot_div] = plotting.cl_plot2(r2, r3)

    else:
        s = 'No such lab'
        n = 0
        plot_script = ''
        plot_div = ''

    dbc.close()

    return render_template('cl36.html', text=s, labname=labname, n=n, script=plot_script, div=plot_div)

@app.route('/c14/<labname>')
def carbon(labname):


    dbc = common.reader_connect_to_db()
    dbcursor = dbc.cursor()

    dbcursor.execute('select distinct _c14_quartz.extraction_lab from _c14_quartz')
    existing_labs = dbcursor.fetchall()
    lab_exists = False
    for lab in existing_labs:
        if labname in lab:
            lab_exists = True

    if lab_exists:

        q1 = """select base_sample.name, base_application.name
            from base_sample, _c14_quartz, base_site, base_application_sites, base_application
            where base_sample.id = _c14_quartz.sample_id
            and base_sample.site_id = base_site.id
            and base_site.id = base_application_sites.site_id
            and base_application_sites.application_id = base_application.id
            and _c14_quartz.extraction_lab = 'XXXX'
            order by base_sample.name """
        q1 = q1.replace('XXXX',labname)
        dbcursor.execute(q1)
        result = dbcursor.fetchall()

        q2 = "select _c14_quartz.N14_atoms_g,_c14_quartz.delN14_atoms_g, iced.base_sample.name, _c14_quartz.extraction_lab from _c14_quartz, iced.base_sample where _c14_quartz.extraction_lab = '" + labname + "' and iced.base_sample.id = _c14_quartz.sample_id"
        dbcursor.execute(q2)
        r2 = dbcursor.fetchall()

        q3 = """select iced._c14_quartz.N14_atoms_g, iced._c14_quartz.delN14_atoms_g
            from iced._c14_quartz
            where iced._c14_quartz.N14_atoms_g is not null
            and iced._c14_quartz.delN14_atoms_g is not null
            and iced._c14_quartz.N14_atoms_g  != 0
            and iced._c14_quartz.extraction_lab != 'XXXX'
            and iced._c14_quartz.delN14_atoms_g  != 0"""
        q3 = q3.replace('XXXX', labname)
        dbcursor.execute(q3)
        r3 = dbcursor.fetchall()

        n = len(result)
        s = []
        for item in result:
            this_link = '<a href="https://version2.ice-d.org/' + item[1] + '/sample/' + item[0] + '" target="_blank">' + item[0] + '</a>'
            s.append(this_link)

        [plot_script,plot_div] = plotting.c_plot2(r2, r3)

    else:
        s = 'No such lab'
        n = 0
        plot_script = ''
        plot_div = ''

    dbc.close()

    return render_template('c14.html', text=s, labname=labname, n=n, script=plot_script, div=plot_div)

@app.route('/')
def fun_examples():

    dbc = common.reader_connect_to_db()
    dbcursor = dbc.cursor()

    q1 = """ select distinct iced. _be10_al26_quartz.N10_atoms_g, iced._be10_al26_quartz.N26_atoms_g, iced.base_sample.elv_m, iced._be10_al26_quartz.delN10_atoms_g, iced._be10_al26_quartz.delN26_atoms_g, iced.base_sample.name
        from iced.base_sample, iced._be10_al26_quartz, iced.base_site, iced.base_application_sites, iced.base_calculatedage
        where iced._be10_al26_quartz.sample_id = iced.base_sample.id
        and iced.base_site.id = iced.base_sample.site_id
        and iced.base_site.id = iced.base_application_sites.site_id
        and iced.base_calculatedage.sample_id = iced.base_sample.id
        and iced.base_sample.elv_m is not null
        and iced._be10_al26_quartz.N10_atoms_g is not null
        and iced._be10_al26_quartz.N26_atoms_g is not null
        and iced.base_sample.elv_m != 0
        and iced.base_sample.what LIKE "%oulder%"
        and iced._be10_al26_quartz.N10_atoms_g != 0
        and iced._be10_al26_quartz.N26_atoms_g != 0
        and iced.base_calculatedage.t_St > 25000
        and iced.base_application_sites.application_id = 2"""
    dbcursor.execute(q1)
    r1 = dbcursor.fetchall()

    n1 = len(r1)

    [plot_script1, plot_div1] = plotting.ratio_elv_plot(r1)

    q1b = """select distinct iced.base_sample.lat_DD, iced.base_sample.lon_DD, iced.base_sample.name
        from iced.base_sample, iced._be10_al26_quartz, iced.base_site, iced.base_application_sites, iced.base_calculatedage
        where iced._be10_al26_quartz.sample_id = iced.base_sample.id
        and iced.base_site.id = iced.base_sample.site_id
        and iced.base_site.id = iced.base_application_sites.site_id
        and iced.base_calculatedage.sample_id = iced.base_sample.id
        and iced.base_sample.elv_m is not null
        and iced._be10_al26_quartz.N10_atoms_g is not null
        and iced._be10_al26_quartz.N26_atoms_g is not null
        and iced.base_sample.elv_m != 0
        and iced.base_sample.what LIKE "%oulder%"
        and iced._be10_al26_quartz.N10_atoms_g != 0
        and iced._be10_al26_quartz.N26_atoms_g != 0
        and iced.base_calculatedage.t_St > 25000
        and iced.base_application_sites.application_id = 2"""
    dbcursor.execute(q1b)
    r1b = dbcursor.fetchall()

    [plot_script1b, plot_div1b] = plotting.geo_map(r1b)

    q2 = """ select distinct iced._c14_quartz.N14_atoms_g, iced.base_sample.elv_m, iced.base_calculatedage.t_St, iced.base_sample.name
        from iced._c14_quartz, iced.base_sample, iced.base_site, iced.base_application_sites, iced.base_calculatedage
        where iced.base_sample.id = iced._c14_quartz.sample_id
        and iced.base_sample.site_id = iced.base_site.id
        and iced.base_site.id = iced.base_application_sites.site_id
        and iced.base_calculatedage.sample_id = iced.base_sample.id
        and iced.base_calculatedage.t_St != 0
        and iced.base_sample.elv_m > 1
        and iced._c14_quartz.N14_atoms_g / iced.base_calculatedage.t_St < 100
        and iced.base_calculatedage.t_St < 25000
        and iced.base_calculatedage.nuclide LIKE "%N14quartz"
        and iced.base_application_sites.application_id = 1"""
    dbcursor.execute(q2)
    r2 = dbcursor.fetchall()

    n2 = len(r2)

    [plot_script2, plot_div2] = plotting.c14_PR(r2)

    q2b = """select distinct iced.base_sample.lat_DD, iced.base_sample.lon_DD, iced.base_sample.name
        from iced._c14_quartz, iced.base_sample, iced.base_site, iced.base_application_sites, iced.base_calculatedage
        where iced.base_sample.id = iced._c14_quartz.sample_id
        and iced.base_sample.site_id = iced.base_site.id
        and iced.base_site.id = iced.base_application_sites.site_id
        and iced.base_calculatedage.sample_id = iced.base_sample.id
        and iced.base_calculatedage.t_St != 0
        and iced.base_sample.elv_m > 1
        and iced._c14_quartz.N14_atoms_g / iced.base_calculatedage.t_St < 100
        and iced.base_calculatedage.t_St < 25000
        and iced.base_calculatedage.nuclide LIKE "%N14quartz"
        and iced.base_application_sites.application_id = 1"""
    dbcursor.execute(q2b)
    r2b = dbcursor.fetchall()

    [plot_script2b,plot_div2b] = plotting.geo_map(r2b)

    q3 = """select iced.base_sample.lon_DD, iced.base_calculatedage.t_St, iced.base_calculatedage.dtint_St, iced.base_sample.name
        from iced.base_sample, iced.base_calculatedage, iced.base_application_sites, iced.base_site
        where iced.base_sample.id = iced.base_calculatedage.sample_id
        and iced.base_sample.site_id = iced.base_site.id
        and iced.base_site.id = iced.base_application_sites.site_id
        and iced.base_application_sites.application_id = 3
        and iced.base_sample.what LIKE "%oulder%"
        and iced.base_sample.lat_DD >= 64.8
        and iced.base_sample.lat_DD <= 71
        and iced.base_sample.lon_DD >= -60
        and iced.base_sample.lon_DD <= -48
        and iced.base_calculatedage.t_St != 0
        and iced.base_calculatedage.t_St is not null;"""
    dbcursor.execute(q3)
    r3 = dbcursor.fetchall()

    n3 = len(r3)

    [plot_script3, plot_div3] = plotting.GrIS_TDD(r3)

    q4 = """select iced.base_sample.lat_DD, iced.base_sample.lon_DD, iced.base_sample.name
        from iced.base_sample, iced.base_application_sites, iced.base_site
        where iced.base_sample.site_id = iced.base_site.id
        and iced.base_site.id = iced.base_application_sites.site_id
        and iced.base_application_sites.application_id = 3
        and iced.base_sample.what LIKE "%oulder%"
        and iced.base_sample.lat_DD >= 64.8
        and iced.base_sample.lat_DD <= 71
        and iced.base_sample.lon_DD >= -60
        and iced.base_sample.lon_DD <= -48"""
    dbcursor.execute(q4)
    r4 = dbcursor.fetchall()

    [plot_script4, plot_div4] = plotting.geo_map(r4)

    q5 = """select left(iced.base_sample.created_at,4), substring(iced.base_sample.created_at,6,2),substring(iced.base_sample.created_at,9,2)
        from iced.base_sample
        where iced.base_sample.id > 21901"""
    dbcursor.execute(q5)
    r5 = dbcursor.fetchall()

    [plot_script5, plot_div5] = plotting.create_at(r5)

    dbc.close()

    return render_template('examples.html', script1=plot_script1, div1=plot_div1, n1=n1, script1b=plot_script1b, div1b=plot_div1b, script2=plot_script2, div2=plot_div2, n2=n2, script2b=plot_script2b, div2b=plot_div2b, script3=plot_script3, div3=plot_div3, n3=n3, script4=plot_script4, div4=plot_div4, script5=plot_script5, div5=plot_div5)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
