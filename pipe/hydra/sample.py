import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(version_base=None, config_path="config", config_name="test")
def my_app(cfg : DictConfig) -> None:
    print(cfg.dev.env)

if __name__ == "__main__":
    my_app()