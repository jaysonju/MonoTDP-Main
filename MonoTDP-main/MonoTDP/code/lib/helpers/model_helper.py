from lib.models.MonoTDP import MonoTDP


def build_model(cfg,mean_size):
    if cfg['type'] == 'MonoTDP':
        return MonoTDP(backbone=cfg['backbone'], neck=cfg['neck'], mean_size=mean_size)
    else:
        raise NotImplementedError("%s model is not supported" % cfg['type'])
