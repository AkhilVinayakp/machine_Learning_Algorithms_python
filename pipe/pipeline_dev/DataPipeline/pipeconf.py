# pipeline configuration
import click
from hydra import compose, initialize
from datapipe_pre import data_loading

@click.group
def pipeline():
    click.echo("configuring system pipeline")

@pipeline.command()
@click.argument('name')
@click.option('--config_dir', default="conf", help="path to the configuration file")
@click.option('--config_name', default="staging.yaml", help="configuration file name")
def run(name, config_dir, config_name):
    """run configuration. quick run"""
    # hydra 
    initialize(config_path=config_dir, version_base=None)
    cfg = compose(config_name=config_name)
    data_loading(cfg.get("datapipe"))


@pipeline.command()
@click.argument('name')
def serve(name):
    """serving pipeline into prefect
    will not trigger.
    """
    # hydra 
    data_loading.serve(name)

if __name__ == "__main__":
    pipeline()