from src.io import load_raw_data


def build_master_dataset() -> DataFrame:

    manual, about_me, about_gig, gig_title = load_raw_data()

    gig_title = gig_title.rename(
        columns={
            "ID": "gig_title_id"
        }
    )

    about_gig = about_gig.rename(
        columns={
            "ID": "about_gig_id"
        }
    )

    about_me = about_me.rename(
        columns={
            "ID": "about_me_id"
        }
    )

    manual = manual.rename(
        columns={
            "Gig Title": "gig_title_id",
            "About the Gig": "about_gig_id",
            "About Me": "about_me_id",
            "Delivery Timeline (days)": "DeliveryTimeline",
        }
    )

    master = manual.copy()

    master = master.merge(
        gig_title,
        on="gig_title_id",
        how="left",
    )

    master = master.merge(
        about_gig,
        on="about_gig_id",
        how="left",
    )

    master = master.merge(
        about_me,
        on="about_me_id",
        how="left",
    )

    return master